import sys
N = input()
if len(N) == 1:
    print(N)
    sys.exit()

s = 0
for x in N:
    s += int(x)

if N[0] != '9' and '9'*(len(N)-1) == N[1:]:
    print(s)
elif N[0] != '9':
    print((int(N[0])-1) + 9*(len(N)-1))
elif '9'*len(N) == N:
    print(s)
else:
    print((int(N[0])-1) + 9*(len(N)-1))