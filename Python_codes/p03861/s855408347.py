a,b,x = map(int, input().split())
if a%x != 0: a += (x-a%x)
if b%x != 0: b -= b%x
ans = b//x - a//x +1 if a <= b else 0
print(ans)