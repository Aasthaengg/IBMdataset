S = input()
W = int(input())
res = ''
for i in range((len(S) + W - 1) // W):
    res = ''.join((res, S[W * i]))
print(res)