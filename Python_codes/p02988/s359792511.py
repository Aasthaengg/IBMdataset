n = int(input())
l = [int(u) for u in input().split()]
res = 0
for i in range(1,n-1):
    if sorted(l[i-1:i+2])[1] == l[i]:
        res += 1
print(res)