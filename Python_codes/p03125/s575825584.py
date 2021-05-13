a,b = map(int,input().split())
ans = 0
if(b % a == 0):
    ans = a + b
else:
    ans = b - a

print(ans)