N=int(input())
k=d=0
while k<=N:
    k+=1
    d=k*(k+1)//2
    if d >= N: break
for i in range(1,k+1):
    if i==d-N: continue
    print(i)