k, a, b = map(int, input().split())
ans = 0
if b - a <= 1: # 叩き続けたほうがいい
    ans = k + 1
else:
    n = k - a + 1 #a個
    if n % 2 == 1:
        ans = a + 1 + (b-a)*(n//2) #最後交換しない
    else:
        ans = a + (b-a)*(n//2) 
print(ans)