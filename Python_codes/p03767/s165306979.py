n = int(input())

a = list(map(int,input().split()))

a.sort(reverse=True)
res = 0
s = 0
for i in range(n):
    res += a[i+1+s]
    s += 1
print(res)