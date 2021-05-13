import collections

S = input()
N = len(S)
num_p = N // 2
c = collections.Counter(S)
ans = num_p - c['p']
print(ans)
