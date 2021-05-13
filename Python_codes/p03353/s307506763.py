s = input().rstrip()
N = len(s)
K = int(input())

c = []
for i in range(N):
    for j in range(i+1, N+1):
        if len(c) < K:
            c.append(s[i:j])
            c.sort()
        else:
            if s[i:j] in c:
                continue

            if c[K-1] < s[i:j]:
                break
            else:
                c[K-1] = s[i:j]
                c.sort()

print(c[-1])
