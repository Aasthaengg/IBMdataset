n = int(input())
A = [0]*n
B = [0]*n
for i in range(n):
    a,b = map(int,input().split())
    A[i]=a%b
    B[i]=b
ans = 0
tmp=0
for i in range(n-1,-1,-1):
    tmp +=(B[i] -(tmp+A[i]))%B[i]
print(tmp)
