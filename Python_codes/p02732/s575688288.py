n = int(input())
a = list(map(int, input().split()))

a_dict = {}
for i in a:
    if a_dict.get(i, False):
        a_dict[i] += 1
    else:
        a_dict[i] = 1

def mC2(m):
    return m * (m - 1) // 2

sum = 0
for v in a_dict.values():
    sum += mC2(v)

for i, k in enumerate(a):
    ans = sum - (a_dict[k] - 1)
    print(ans)