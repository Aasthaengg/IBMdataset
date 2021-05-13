w,a,b = map(int, input().split())

if (b <= a+w <= b+w) : ans = 0
else : ans = min(abs(a-(b+w)), abs(a+w-b))
print(ans)