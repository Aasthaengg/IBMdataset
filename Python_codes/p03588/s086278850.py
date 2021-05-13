n = int(input())
bottom = 10 ** 9+7
person = 0

for _ in range(n):
    a, b = map(int, input().split())
    if b < bottom:
        person = max(person, a)
        bottom = b

ans = person + bottom
print(ans)
