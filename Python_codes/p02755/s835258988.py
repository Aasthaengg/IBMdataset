A, B = map(int, input().split())
MAX = 10 ** 3 + 1
res = -1
for i in range(1, MAX):
    if int(0.08 * i) == A and int(0.1 * i) == B:
        res = i
        break
print(res)