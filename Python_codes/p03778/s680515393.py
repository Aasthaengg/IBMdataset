W,a,b = map(int,input().split())

ans = max(b-a-W,a-b-W,0)
print(ans)