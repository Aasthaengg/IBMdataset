a,b,c = map(int,input().split())
ans = min(abs(a-b)+abs(b-c),abs(a-c)+abs(b-c),abs(a-c)+abs(a-b))
print(ans)
