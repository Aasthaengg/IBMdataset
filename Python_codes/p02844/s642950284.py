N = int(input())
S = input()
d = {}
k1 = [0 for i in range(10)]
for i in range(N-2):
    if k1[int(S[i])] != 0: continue
    k1[int(S[i])] += 1
    k2 = [0 for i in range(10)]
    for j in range(i+1, N-1):
        if k2[int(S[j])] != 0: continue
        k2[int(S[j])] += 1
        for k in range(j+1, N):
            st = ''.join([S[i], S[j], S[k]])
            d[st] = True
print(len(d))