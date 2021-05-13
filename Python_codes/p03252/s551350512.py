import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


alphabet = [chr(i+97) for i in range(26)]
dS,dT = {},{}
for s in alphabet:
    dS[s] = []
    dT[s] = []

S,T = LS2(),LS2()
N = len(S)
for i in range(N):
    dS[S[i]].append(i)
    dT[T[i]].append(i)

count_S,count_T = [0]*N,[0]*N  # Si,Ti と同じ文字が何回現れるか
for i in range(N):
    count_S[i] = len(dS[S[i]])
    count_T[i] = len(dT[T[i]])

print('Yes' if count_S == count_T else 'No')
