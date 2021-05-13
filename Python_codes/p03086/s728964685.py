S = input()

base = ['A', 'T', 'G', 'C']

ans = ''
a = ''
for i in range(len(S)):
    if S[i] in base:
        a += S[i]
        if len(a) > len(ans):
            ans = a
    else:
        a = ''
print(len(ans))
