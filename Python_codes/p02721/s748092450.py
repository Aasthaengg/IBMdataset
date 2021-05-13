# import time

N, K, C = list(map(int, input().split()))
S = list(input())

F = []
L = []

# t1 = time.time()
# for i in range(N):
#     if S[i] == 'o':
#         if len(F) == 0:
#             F.append(i)
#         elif F[-1] + C < i:
#             F.append(i)
#     if len(F) >= K:
#         break
# print(F)
# t2 = time.time()
i = 0
while len(F) <= K and i < N:
    if S[i] == 'o':
        if len(F) == 0:
            F.append(i)
        elif F[-1] + C < i:
            F.append(i)
    i += 1
# print(F)
# t3 = time.time()

# print(t2 - t1, t3 - t2)

i = N - 1
while len(L) <= K and i >= 0:
    if S[i] == 'o':
        if len(L) == 0:
            L.append(i)
        elif L[-1] - C > i:
            L.append(i)
    i -= 1

if len(F) == K and len(L) == K:
    ans = [i + 1 for i in set(F) & set(L)]
    if len(ans) != 0:
        ans.sort()
        [print(i) for i in ans]