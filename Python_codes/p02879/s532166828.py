a,b = map(int, input().split())
aa = a if a < 10 else 0
bb = b if b < 10 else 0

print(-1 if aa*bb == 0 else aa*bb)