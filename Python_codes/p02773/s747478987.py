N = int(input())
num = {}
for i in range(N):
    S = input()
    if S in num:
        num[S] += 1
    else:
        num[S] = 1

max = max(num.values())
keys = []
for k, v in num.items():
    if v == max:
        keys.append(k)
keys.sort()

for key in keys:
    print(key)
