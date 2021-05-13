S = [s for s in input()]
K = int(input())
N = len(S)

# print(S, K)

ord_a = ord('a')

T = [0]*N
for i in range(N):
    s = S[i]
    a = ord(s)
    r = (ord_a + 26 - a) % 26
    if r <= K:
        K -= r
        s = 'a'
    T[i] = s
if K > 0:
    t = T[N - 1]
    a = ord(t)
    a = ord_a + (a - ord_a + K) % 26
    T[N - 1] = chr(a)
print(''.join(T))
