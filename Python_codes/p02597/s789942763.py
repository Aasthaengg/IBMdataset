N = int(input())
ccc = input()
R = ccc.count('R')
ans = 0
for i in range(R):
    if ccc[i] == 'W':
        ans += 1
print(ans)
