from bisect import bisect
S = input()
T = input()

NS = len(S)
NT = len(T)
alp = {}
for i in range(26):
    alp[chr(97+i)] = i
D = [[] for i in range(26)]
for i in range(NS):
    D[alp[S[i]]].append(i)
inf = float("inf")
for i in range(26):D[i].append(inf)
k = 0
l = -1
ans = -1
for i in range(NT):
    index = alp[T[i]]
    if D[index] == [inf]:break
    b = bisect(D[index],l)
    if D[index][b]==inf:
        k += 1
        l = D[index][0]
    else:
        l = D[index][b]
    if i==NT-1:ans = k*NS+l+1
print(ans)