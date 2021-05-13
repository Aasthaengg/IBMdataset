N=int(input())
cnt=0
max=10**6
but=0
id=0
for i in range(1,max,1):
    cnt=cnt+i
    if cnt>=N:
        buf=cnt-N
        break
id=i
seq=[i+1 for i in range(id)]
for i in range(len(seq)):
    if seq[i]!=buf:
        print(seq[i])