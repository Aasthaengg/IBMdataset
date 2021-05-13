x = int(input())
a = int(input())
b = int(input())

ans = x - a
ans = ans - b*(ans//b)
print(ans)