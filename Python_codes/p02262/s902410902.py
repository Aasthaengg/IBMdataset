
# shell sort
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D

import sys
readline = sys.stdin.buffer.readline
cnt = 0


def insersion_sort(A: list, n: int, g: int):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v
    return


def shell_sort(A: list, n: int):
    # 数列 G = {1,4,13,40,121,363,...}を生成
    G = []
    h = 1
    while h <= n:
        G.append(h)
        h = h * 3 + 1
    G = G[::-1]
    print(len(G))
    print(" ".join([str(g) for g in G]))
    for g in G:
        insersion_sort(A, n, g)
    return A


n = int(readline())
A = []

for _ in range(n):
    A.append(int(readline()))

shell_sort(A, n)
print(cnt)
for a in A:
    print(a)

