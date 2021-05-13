n,d = map(int,input().split())
ans = n//(2*d+1)
ans += n%(2*d+1) != 0
print(ans)