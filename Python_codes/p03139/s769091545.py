n,a,b = map(int,input().split())

ans = []

ans.append(min(a,b))
ans.append(max(0,a+b-n))

print(*ans)