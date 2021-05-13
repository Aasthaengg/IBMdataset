N = int(input())
a = list(map(int, input().split()))

cnt = 0
cnt1 = 0
for i in range(len(a)):
    if(a[i]%4==0):
        cnt += 1
    elif(a[i]%2 == 0):
        cnt1 += 1

if(cnt+cnt1//2 >= N//2):
    print("Yes")
else:
    print("No")