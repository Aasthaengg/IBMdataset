n, m, L = map(int, input().split())
  
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
c = [[sum(aaa * bk for aaa, bk in zip(ar,bbb)) for bbb in zip(*b)] for ar in a]
  
for ccc in c:
    print(*ccc)