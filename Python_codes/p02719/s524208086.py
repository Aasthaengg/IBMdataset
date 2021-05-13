n,k = map(int,input().split())

top = n - n//k*k
low = n - ((n//k)+1)*k

ans = min(abs(top),abs(low))
print(ans)