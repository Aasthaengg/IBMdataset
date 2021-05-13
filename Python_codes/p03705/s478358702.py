N,A,B = map(int,input().split())
ans = (N-2) * (B -A) + 1
print(ans if ans >= 0 else 0)