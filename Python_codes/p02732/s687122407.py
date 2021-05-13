n = int(input())
a = list(map(int, input().split()))

d = [0]*n
for i in a:
    d[i-1] += 1

ans = 0
for i in range(n):
    ans += int((d[i]*(d[i]-1))/2)

for i in range(n):
    print(ans-(d[a[i]-1]-1))