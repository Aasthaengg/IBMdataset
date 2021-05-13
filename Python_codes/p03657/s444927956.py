A, B = map(int, input().split())
ans = 'Possible' if any(x % 3 == 0 for x in [A, B, A + B]) else 'Impossible'
print(ans)
