import collections

N = int(input())
s = [input() for i in range(N)]

M = int(input())
t = [input() for j in range(M)]

S = collections.Counter(s)
T = collections.Counter(t)

S.most_common()
T.most_common()

ans = S - T

try:
    print(ans.most_common()[0][1])
except:
    print('0')