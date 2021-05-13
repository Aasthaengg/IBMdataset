n = int(input())
d = list(map(int,input().split()))
sort_d = sorted(d)
#print(sort_d)
tmp = n//2
#print(sort_d[tmp],sort_d[tmp-1])
if sort_d[tmp-1]==sort_d[tmp]:
    print(0)
else:
    print(sort_d[tmp]-sort_d[tmp-1])