a,b = map(int,input().split())
tmp = b-a

num = tmp*(tmp+1)//2

ans = num-b

print(ans)