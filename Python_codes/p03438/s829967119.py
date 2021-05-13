n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
for i in range(n):
    if a[i] < b[i]:
        c += -((a[i]-b[i])//2)
        a[i] += -((a[i]-b[i])//2) * 2
d = 0
for i in range(n):
    if b[i] < a[i]:
        d += a[i]-b[i]
if c == d:
    ans = 1
elif c < d:
    ans = 0
elif d < c:
    ans = 1
print(["No","Yes"][ans])