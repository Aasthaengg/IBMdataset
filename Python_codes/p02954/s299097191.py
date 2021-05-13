s=input()
l=['0' for _ in s]
ind=0
for i in range(len(s)):
    if s[i]=='R':
        ind=i
    elif (i-ind)%2==0:
        l[ind]=str(int(l[ind])+1)
    else:
        l[ind+1]=str(int(l[ind+1])+1)

for i in range(1,len(s)+1):
    if s[-i]=='L':
        ind=-i
    elif (-i-ind)%2==0:
        l[ind]=str(int(l[ind])+1)
    else:
        l[ind-1]=str(int(l[ind-1])+1)
print(' '.join(l))
