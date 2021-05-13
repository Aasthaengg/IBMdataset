import sys
input = sys.stdin.readline

a,b,c,k = list(map(int,input().split()))
if k<a:
    print(k)

elif k<=a+b:
    print(a)
else:
    print(a-1*(k-a-b))
