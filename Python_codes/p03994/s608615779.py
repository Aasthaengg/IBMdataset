N = 26
ord_a = ord('a')
S = [ord(s) - ord_a for s in input()]
K = int(input())


for i in range(len(S)):
    r = (N - S[i]) % N
    if K >= r:
        K -= r
        S[i] = 0


S[-1] += K % N
S[-1] %= N

answer = ''.join(chr(s + ord_a) for s in S)
print(answer)
