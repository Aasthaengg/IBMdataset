n = int(input())
a = list(map(int, input().split()))

ans = 0
for el in a:
    twos = 0
    while el and el%2 == 0:
        el = el//2
        twos += 1
    ans += twos
print(ans)