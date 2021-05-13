a,b,c,d = map(int, input().split())
rectangle1 = a * b
rectangle2 = c * d
ans = max(rectangle1, rectangle2)
print(ans)