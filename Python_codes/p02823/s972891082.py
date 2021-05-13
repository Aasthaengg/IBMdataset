n,a,b = map(int, input().split())

dist = b - a
if dist % 2 == 0:
    print(dist//2)
elif a - 1 < n - b:
    print(a-1 + 1 +(b-a-1)//2)
else:
    print(n - b + 1 +(b-a-1)//2)