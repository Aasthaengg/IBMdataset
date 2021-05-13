import sys
sys.setrecursionlimit(10**6)

a=list(map(int,input().split()))

newa=sorted(a)

#print(a)
#print(newa)
#print(newa[2])

if newa[2]%2==0 or newa[1]%2==0 or newa[0]%2==0:
    print("0")
else:
    print(newa[0]*newa[1])