n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
da = 0
db = 0
for i in range(n):
    if a[i] > b[i]:
        db += a[i]-b[i]
    else:
        da += (b[i]-a[i])//2
if db > da:
    print("No")
else:
    print("Yes")
