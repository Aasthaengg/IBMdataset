i = list(map(int, input().split()))

c = i[0] * i[1]

ans = 'Even' if c % 2 == 0 else 'Odd'
print(ans)