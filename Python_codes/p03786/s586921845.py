import numpy as np

N=int(input())
A=list(map(int, input().split()))
A=sorted(A, reverse=True)

#print(now) #普通に全部食える


cum=np.cumsum(A[::-1])[::-1]
adds=[-1]*(N)
adds[0]=cum[0]
for i in range(1,N):
    if cum[i]*2>=A[i-1]:
        adds[i]=adds[i-1]
    else:
        adds[i]=cum[i]
#print(A)
#print(cum)
#print(adds)
adds=np.array(adds)
ans=(adds==cum[0]).sum()

print(ans)