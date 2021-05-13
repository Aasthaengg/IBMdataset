S = input()
K = int(input())
prev = S[0]
compressed = [1]
for c in S[1:]:
    if c == prev:
        compressed[-1] += 1
    else:
        prev = c
        compressed.append(1)
if len(compressed) == 1:
    print(len(S) * K // 2)
else:
    ans = sum(cnt // 2 for cnt in compressed) * K
    if S[0] == S[-1]:
        tmp = (compressed[0] + compressed[-1]) // 2
        tmp -= compressed[0] // 2
        tmp -= compressed[-1] // 2
        ans += tmp * (K - 1)
    print(ans)
