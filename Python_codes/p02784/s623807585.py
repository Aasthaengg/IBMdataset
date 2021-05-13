h,a = [int(i) for i in input().split()]

m = [int(i) for i in input().split()]

ans='No'

if h<=sum(m): ans='Yes'

print(ans)
