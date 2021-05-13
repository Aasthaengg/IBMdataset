a,b = map(int,input().split())
if a <= b:
    ans = a
elif a == 1:
    ans = 1
else:
    ans = a-1
print(ans)