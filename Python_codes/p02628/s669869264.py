N, K = map(int,input().split())
p = list(map(int,input().split()))

p_sort = p.sort()
p_sort_K = p[0:K]
print(sum(p_sort_K))