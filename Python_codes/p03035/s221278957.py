a,b = map(int,input().split())
if 13 <= a:
    ans = b
elif 6 <= a and a <=12:
    ans = b//2
elif a <= 5:
    ans = 0
print(ans)