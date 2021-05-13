L,R,d = map(int,input().split())

left = (L-1)//d
right = R//d
ans = right-left
print(ans)