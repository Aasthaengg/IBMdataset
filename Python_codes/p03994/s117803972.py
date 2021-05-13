S = input()
S = list(S)

def func(c) -> int:
    t = 26 - (ord(c) - ord('a'))
    t %= 26
    return t

L = [func(c) for c in S]
#print(L)
K = int(input())
for i in range(len(L)):
    if(L[i] <= K):
        K -= L[i]
        L[i] = 0
    else:
        continue
#print(L)
if(K > 0):
    #L[-1]
    K %= 26
    L[-1] -= K
    if(L[-1] < 0):
        L[-1] += 26

def gunc(c):
    t = 26 - c
    t %= 26
    return chr(t+97)
ans = [gunc(c) for c in L]
st = ''
for c in ans:
    st += c
print(st)