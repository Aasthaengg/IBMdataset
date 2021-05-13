s=input()
N=len(s)

ind_a=0
ind_z=0
for i in range(N):
    if s[i]=="A":
        ind_a=i
        break
for i in range(1,N+1):
    if s[-i]=="Z":
        ind_z=N-i
        break

print(ind_z-ind_a+1)