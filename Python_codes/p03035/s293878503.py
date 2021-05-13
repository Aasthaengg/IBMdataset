a,b = map(int,input().split())
if a>12:
    ans = b
elif a>5:
    ans = b//2
else:
    ans = 0
print(ans)
