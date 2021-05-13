S = raw_input()
w = int(raw_input())

res = ''
i = 0
while i<len(S):
    res += S[i]
    i+=w

print res