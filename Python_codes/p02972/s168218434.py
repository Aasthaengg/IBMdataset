import sys
input = sys.stdin.readline
N = int(input())
a =[0]+ list(map(int, input().split()))
for i in range(N,0,-1):
    a[i] =sum(a[i::i]) %2

print(sum(a))
del a[0]
for i,v in enumerate(a):
    if v==1:
        print(i+1,end=" ")