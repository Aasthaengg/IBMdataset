from itertools import combinations_with_replacement

N = int(input())
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
DP = [set() for _ in range(N)]
DP[0].add((1, 'a'))

for i in range(1, N):
    for num, s in DP[i-1]:
        for j in range(num):
            DP[i].add((num, s + C[j]))
        DP[i].add((num + 1, s + C[num]))
A = []
for _, ax in DP[N-1]:
    A.append(ax)
A.sort()
for a in A:
    print(a)




