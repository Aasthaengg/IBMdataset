S = list(input())
T = list(input())
N = len(S)

a = ord('a')
alf = []
for i in range(26):
     alf.append(chr(a))
     a += 1

SN = [[] for i in range(26)]
TN = [[] for i in range(26)]
for i in range(N):
    for j in range(26):
        if alf[j] == S[i]:
            SN[j].append(i)
        if alf[j] == T[i]:
            TN[j].append(i)
SN.sort()
TN.sort()
print('Yes' if SN == TN else 'No')
