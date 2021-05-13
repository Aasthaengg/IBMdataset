n,k,s=[int(i) for i in input().split()]

for i in range(k):
    print(s,end="")
    print(' ',end="")

if(s!=10**9):
    for i in range(n-k):
        print(s+1,end="")
        print(' ',end="")
else:
    for i in range(n-k):
        print(1,end="")
        print(' ',end="")


