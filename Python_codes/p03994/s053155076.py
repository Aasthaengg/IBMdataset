S = input()
K = int(input())

N = len(S)
T = list(S)
for i in range(N - 1):
    if T[i] == 'a':
        continue
    if K >= ord('z') - ord(T[i]) + 1:
        K -= ord('z') - ord(T[i]) + 1
        T[i] = 'a'

T[N - 1] = chr(ord('a') + (ord(T[N - 1]) - ord('a') + K) % 26)
print("".join(T))