N = int(input())
S = input()

a = [0]*N

for i in range(1, N):
    b = []
    for s in S[:i]:
        if s in S[i:] and s not in b:
            a[i] += 1
            b.append(s)

print(max(a))
