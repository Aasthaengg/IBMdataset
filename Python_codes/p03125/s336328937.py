a,b = map(int,input().split())
ans = a+b
if b % a != 0:
    ans = b-a
print(ans)
