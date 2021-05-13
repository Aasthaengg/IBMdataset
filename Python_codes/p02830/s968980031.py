N = int(input())
S, T = [s for s in input().split(' ')]
ret = ''
for s, t in zip(S, T):
    ret += s + t
print(ret)
