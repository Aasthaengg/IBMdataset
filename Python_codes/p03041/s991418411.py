N, K = map(int, input().split())
S = input()
ret = ""
for i,s in enumerate(S):
    if i+1==K:
        ret += str.lower(s)
    else:
        ret += s
print(ret)