n = int(input())
s = [input() for _ in range(n)]

cnt = {"AC":0, "WA":0, "TLE":0, "RE":0}

for i in s:
    cnt[i] += 1

for i, j in cnt.items():
    print(f'{i} x {j}')