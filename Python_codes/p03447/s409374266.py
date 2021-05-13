x = int(input())
a = int(input())
b = int(input())
ans = x - a
while ans >= b:
    ans -= b
print(ans)
