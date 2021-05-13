n = int(input())
v = list(map(int,input().split()))
sort_v = sorted(v)
ans = 0
tmp = sort_v[0]
for i in range(1,n):
    tmp = (tmp + sort_v[i])/2
print(tmp)
