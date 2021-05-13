n =int(input())
AB = []
Sb = 0
for i in range(n):
    a, b = map(int, input().split())
    AB.append(a+b)
    Sb += b

AB.sort()
ans = 0
for i in range(n):
    if i%2 == 0:
        ans += AB.pop()
    else:
        AB.pop()
ans -= Sb
print(ans)
