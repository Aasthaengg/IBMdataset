import sys
X=int(input())
l=[i**5 for i in range(1000)]
for i in range(1000):
    for j in range(-999,0):
        if l[i]+l[j*-1]==X:
            print(i,j)
            sys.exit()
    for j in range(i):
        if l[i]-l[j]==X:
            print(i,j)
            sys.exit()