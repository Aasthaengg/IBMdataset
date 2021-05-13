n = int(input())
mul = lambda x: x * 100 + x * 10 + x
if mul(n//100)>=n:ans = mul(n//100)
else :ans = mul(n//100+1)
print(ans)