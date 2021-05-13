s = input().split()

n = int(s[0])
t = int(s[1])

arrays = []

for i in range(n):
    v = input().split()
    w = int(v[1])
    if w <= t:
        arrays.append(int(v[0]))

arrays.sort()
if len(arrays) == 0:
    print('TLE')
else:
    answer = arrays[0]
    print(answer)