N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
D = []
i = 1
while i * i <= S:
    if S % i == 0:
        D.append(i)
        if S // i != i:
            D.append(S // i)
    i += 1

D = sorted(D, reverse=True)

for d in D:
    mod = [a % d for a in A]
    mod = sorted(mod)
    s = sum(mod)
    if sum(mod[:-s//d]) <= K:
        print(d)
        exit()

