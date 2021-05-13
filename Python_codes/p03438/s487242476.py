n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cou = sum(b) - sum(a)
ac = 0
bc = 0
for i in range(n):
    if a[i] < b[i]:
        if (b[i] - a[i]) % 2 == 0:
            ac += (b[i]-a[i])//2
        elif (b[i] - a[i]) % 2 == 1:
            ac += (b[i]-a[i])//2 + 1
            bc += 1
    elif a[i] > b[i]:
        bc += a[i]-b[i]
if ac > cou or bc > cou:
    print("No")
else:
    if cou - bc == (cou-ac)*2:
        print("Yes")
    else:
        print("No")