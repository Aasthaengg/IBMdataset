n = int(input())
ls = [0 for i in range(10 ** 5)]
lsa = list(map(int,input().split()))

for i in range(len(lsa)):
    ls[lsa[i] - 1] += 1

ans1 = sum(lsa)
ansls = []

q = int(input())

for i in range(q):
    b, c = map(int,input().split())
    if i == 0:
        ans = ans1 + ((c - b) * ls[b - 1])
    else:
        ans = ansls[-1] + ((c - b) * ls[b - 1])
    ansls.append(ans)
    ls[c - 1] += ls[b - 1]
    ls[b - 1] = 0

for i in range(q):
    print(ansls[i])
