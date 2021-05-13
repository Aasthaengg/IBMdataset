n, c, k=map(int,input().split())
bus=1
pssgr=0
fst_pssgr=0
t_lst=[]
for i in range(n):
    t=int(input())
    t_lst.append(t)

t_lst.sort()

for i in range(n):
    if t_lst[i]-t_lst[fst_pssgr]>k:
        bus+=1
        pssgr=1
        fst_pssgr=i
        continue
    pssgr+=1
    if pssgr==c and i<n-1:
        bus+=1
        pssgr=0
        fst_pssgr=i+1

print(bus)