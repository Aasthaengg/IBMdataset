S = list(input())
w = int(input())

r = ''
for i in range(0, len(S), w):
    r += S[i]
print(r)