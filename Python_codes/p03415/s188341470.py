C = [list(input()) for _ in range(3)]
ans = [c for i, ci in enumerate(C) for j, c in enumerate(ci) if i == j]
print(''.join(ans))