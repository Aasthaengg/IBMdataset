n = int(input())
a = list(map(int,input().split()))
count4 = 0
count2 = 0
for i in a:
    if i%4 == 0:
        count4 += 1
    elif i%2 == 0:
        count2 += 1
if (n//2) <= count4:
    print("Yes")
elif (n-(count4*2) <= count2):
    print("Yes")
else:
    print("No")