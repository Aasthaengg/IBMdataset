import sys
s=input().split()
r=int(s[0]);c=int(s[1])
a=[[0 for j in range(c)] for i in range(r)]
b=[[0 for j in range(c+1)]for i in range(r+1)]
for i in range(r):
    t=input().split()
    for j in range(c):
        a[i][j]=int(t[j])
        b[i][j]=a[i][j]
        b[r][j]+=a[i][j]
        b[i][c]+=a[i][j]
        b[r][c]+=a[i][j]
for i in range(r+1):
    for j in range(c+1):
        sys.stdout.write("{0}".format(b[i][j]))
        if j==c:
            sys.stdout.write("\n")
        else:
            sys.stdout.write(" ")