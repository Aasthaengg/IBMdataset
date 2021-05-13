N, K = map(int, input().split())
hhh = list(map(int, input().split()))
hhh.sort()
print(sum(hhh[:-K]) if K > 0 else sum(hhh))
