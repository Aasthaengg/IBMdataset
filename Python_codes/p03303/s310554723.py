S = str(input())
w = int(input())

if len(S) % w == 0:
    L = len(S) // w
else:
    L = len(S) // w + 1

moji = str()

for i in range(L):
    moji = moji + S[i* w]

print(moji) 