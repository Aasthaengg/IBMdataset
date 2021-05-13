N=int(input());s=input();
c=0
for i in range(N):
    if s[i]=='R':
        c+=1
    else:
        c-=1

print("Yes" if c>0 else "No")