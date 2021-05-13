n = int(input())

num_e = 1
num = num_e**2 + num_e

l = []


ok = 0

while num//2 <= 10**5:
    if num // 2 == n:
        ok = 1
        break

    num_e += 1
    num = num_e**2 + num_e

if not ok:
    print('No')
else:
    print('Yes')
    ans = [[num_e] for i in range(num_e+1)]

    num = 1
    for i in range(num_e):
        for j in range(i+1):
            ans[j].append(num)
            ans[i+1].append(num)
            num += 1
    print(num_e+1)
    for i in range(num_e+1):
        print(' '.join(map(str, ans[i])))
