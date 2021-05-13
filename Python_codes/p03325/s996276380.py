N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    if a % 2 == 1:
        continue

    ans += format(a, 'b')[::-1].find('1')
print(ans)
