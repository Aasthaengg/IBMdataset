n,m = map(int,input().split())
ac = n - m if n > m else 0
ans = (ac*100 + (1900*m))*(2**m)
print(ans)