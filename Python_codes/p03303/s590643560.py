S = input()
w = int(input())
iter = int((len(S) - 1) / w) + 1
s = ''

for i in range(iter):
    s += S[w*i]

print(s)
