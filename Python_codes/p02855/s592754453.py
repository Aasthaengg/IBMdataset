# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

A = []
color = 1
for s in S:
    c = s.count("#")
    if c == 1:
        A.append([color] * len(s))
        color += 1
    elif c >= 2:
        l = []
        i = -1
        j = s.find("#")
        while j != -1:
            l += [color] * (j - i)
            color += 1
            i, j = j, s.find("#", j + 1)
        l += [color - 1] * (len(s) - i - 1)
        A.append(l)
    else:
        A.append(s)
exist = 0
for i, s in enumerate(S):
    if "#" in s:
        exist = i
        break

for i in reversed(range(exist)):
    if "." in A[i]:
        A[i] = A[i + 1]

for i in range(exist + 1, len(A)):
    if "." in A[i]:
        A[i] = A[i - 1]

for a in A:
    print(*a)
