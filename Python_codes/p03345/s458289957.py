A,B,C,K  = map(int,input().split())
ans = int((A-B)*((-1)**K))
print(ans if abs(ans)< 1e18 else "Unfair")
