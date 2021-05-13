N = int(input())
s = input()
t = input()
l = 2*N
kouho = []

for i in range(N):
    ns = s[i:]
    res = 0
    for j, k in zip(ns, t):
        if j == k:
            res += 1
        else:
            break
    kouho.append(res)

print(l - max(kouho))
