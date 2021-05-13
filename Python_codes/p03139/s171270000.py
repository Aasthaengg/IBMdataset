n, a, b = map(int, input().split())
print(min(a,b), end=" ")
if n >= a+b:
    print(0)
else:
    print(a+b-n)