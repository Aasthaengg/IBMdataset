n,m = map(int,input().split())
ans = min(n,m//2) + max(0,(m-2*n)//4)
print(ans)
