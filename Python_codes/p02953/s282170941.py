import sys
n=int(input())
h=list(map(int,input().split()))
for i in range(n-1):
    if h[-i-2]>h[-i-1]:
        if h[-2-i]==h[-i-1]+1:
            h[-2-i]-=1
        else:
            print("No")
            sys.exit()
print("Yes")
    

