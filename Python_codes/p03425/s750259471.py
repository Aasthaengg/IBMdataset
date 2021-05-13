from itertools import combinations
N = int(input())
name = [0]*5
ans = 0
for i in range(N):
    a = input()
    if a[0] == 'M': name[0] += 1
    elif a[0] == 'A': name[1] += 1
    elif a[0] == 'R': name[2] += 1
    elif a[0] == 'C': name[3] += 1
    elif a[0] == 'H': name[4] += 1
if sum(name) < 3:
    print(0)
else:
    for i in combinations(name, 3):
        ans += i[0]*i[1]*i[2]
    print(ans)

