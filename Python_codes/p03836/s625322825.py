a, b, c, d = map(int, input().rstrip().split())
x = c - a
y = d - b
result1 = "U"*y+"R"*x
result2 = "D"*y+"L"*x
print(result1+result2+"LU"+result1+"RD"+"RD"+result2+"LU")