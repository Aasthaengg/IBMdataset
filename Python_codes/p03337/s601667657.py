a,b=map(int,input().split())
sum = a + b
deg = a - b
mul = a * b
ans = max(sum,deg,mul)
print(ans)
