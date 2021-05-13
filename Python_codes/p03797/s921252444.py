S, C = map(int, input().split(' '))

scc = min(S, C // 2)

C -= scc * 2

print(scc + C // 4)
