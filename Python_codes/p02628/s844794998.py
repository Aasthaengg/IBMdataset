N,K = map(int,input().split())
p = list(map(int,input().split()))
p_sorted = sorted(p)
print(sum(p_sorted[:K]))