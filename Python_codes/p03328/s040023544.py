a,b = map(int,input().split())
ret = b-a
ans = ret*(ret+1)//2
print(ans-b)
