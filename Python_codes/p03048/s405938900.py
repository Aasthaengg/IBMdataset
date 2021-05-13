*s,n=map(int,input().split())
s.sort()
c=0
for i in range(n//s[2]+1):
    for j in range(n//s[1]+1):
        if (n-s[2]*i-s[1]*j)%s[0] == 0 and 0<=(n-s[2]*i-s[1]*j):
            #print(i,j,n-s[2]*i-s[1]*j)
            c+=1
print(c)