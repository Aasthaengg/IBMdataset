#6
#入力
N=int(input())

#処理
import math as m
t=0
for i in range(m.ceil(N/4),m.floor(N*3/4)+1):
    #print(i)
    if 4*i==N:
        continue
    for j in range(m.ceil(N*i/(4*i-N)),m.floor(2*N*i/(4*i-N))+1):
        #print(j)
        if 4*i*j-N*i-N*j==0:
            continue
        k=int((N*i*j)/(4*i*j-N*i-N*j))
        #print(k)
        if 4*i*j*k==N*(i*j+i*k+j*k):
            h=i
            n=j
            t=1
            break
    if t==1:
        break

print(h,n,k)
