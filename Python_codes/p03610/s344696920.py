s = input()
l = len(s)
o = l//2
S = ''

if l%2== 0:
    for i in range(o):
        S += s[2*i]
if l%2 == 1:
    for i in range(o+1):
        S += s[2*i]

print(S)