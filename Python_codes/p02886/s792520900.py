N = int(input())
d = list(map(int,input().split()))

S = []
for i in range(N):
    for t in range(i):
        if i != t:
            S.append(d[i]*d[t])
print(sum(S))