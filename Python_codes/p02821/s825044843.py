import numpy as np

N ,M= map(int,input().split())
l=list(map(int,input().split()))
n0 = 2**int(np.ceil(np.log2(2*(max(l))-1)))

A = np.zeros(n0)

for i in range(N):
    A[l[i]-1]+=1

C = np.fft.ifft( np.fft.fft(A)*np.fft.fft(A) )
ans=0
j=2
q=[]
for ci in np.real(C[:2*(max(l))-1] + 0.5):
    q.append([int(ci),j])
    j+=1
#int(ci):足してjになる組み合わせの個数
q.reverse()
#print(q)
z=0
j=0
while z<M:
    ans+=q[j][0]*q[j][1]
    z+=q[j][0]
    j+=1
ans-=(z-M)*q[j-1][1]
print(ans)
