n = int(input())

a = list(map(int,input().split()))

cnt_1 = 0
cnt_2 = 0
for i in a:
    if i%4 == 0:
        cnt_1 += 1
    elif i%2 == 0:
        cnt_2 += 1
    
cnt_2 //=2

total = cnt_1 + cnt_2

if len(a)//2 <= total:
    print("Yes")
else:
    print("No")