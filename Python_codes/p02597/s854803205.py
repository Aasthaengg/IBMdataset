N = int(input())
C=list(input())
type=set(C)
L=0
R=0
RR=0
X=0
if 'R' in type and 'W' in type:
    for L in range(N):
      R=RR
      if L>=N-1-R:
        break
      if C[L]=='W':
          for ii in range(N-L-R):
            if C[N-1-R-ii]=='R':
              C[L]='R'
              C[N-1-R-ii]='W'
              X+=1
              break
            RR+=1
            if L>=N-1-R:
              break
print(X)