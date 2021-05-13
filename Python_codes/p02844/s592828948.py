N=int(input())
S=list(input())
#print(S)
SETF=[set() for i in range(N)]
SETE=[0 for i in range(N)]
ANSSET=set()
SETF[0]=set()
SETF[0].add(S[0])
#print(SETF)
#print(type(SETF[1]))
import copy
for i in range(1,N):
    SETF[i]=copy.deepcopy(SETF[i-1])
    SETF[i].add(S[i])
#print(SETF)

SETE[0]=set()
SETE[0].add(S[-1])
#print(SETE)
for i in range(1,N):
    SETE[i]=copy.deepcopy(SETE[i-1])
    SETE[i].add(S[N-1-i])
SETE=SETE[::-1]

for i in range(1,N-1):
    for f in SETF[i-1]:
        for e in SETE[i+1]:
            ANSSET.add(f+S[i]+e)
print(len(ANSSET))
#print(SETE)