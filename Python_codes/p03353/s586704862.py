S = input().strip()
K = int(input())

L = set(list(S))

for j in range(1, 5):
    for i in range(len(S)-j):
        L.add(S[i:i+j+1])

tmp = list(L)
tmp.sort()
print(tmp[K-1])
