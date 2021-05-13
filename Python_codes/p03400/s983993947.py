n = int(input())
d,x = map(int, input().split())
a = [int(input()) for i in range(n)]
num = [1]*(d+1)
for h in range(n):
    for j in range(1,d+1,a[h]):
        x += num[j]
print(x)