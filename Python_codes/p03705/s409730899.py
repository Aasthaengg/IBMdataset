n,a,b = map(int,input().split())
ans = 0
if a > b:
    ans = 0
elif a == b or n == 2:
    ans = 1
elif n > 2:
    ans = (n-2)*(b-a)+1
print(ans)
