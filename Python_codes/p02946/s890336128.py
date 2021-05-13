k,x = map(int,input().split())

ans = list(range(x-k+1,x+k))
ans =[str(a) for a in ans]
ans = " ".join(ans)
print(ans)