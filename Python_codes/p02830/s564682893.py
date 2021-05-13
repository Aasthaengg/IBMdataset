N = int(input())
S, T = input().split()
res = ""
for s, t in zip(S, T):
    res += s + t
print(res)