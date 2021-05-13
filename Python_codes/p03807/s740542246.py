N=int(input())
A=list(map(int,input().split()))
S=0
for i in A:
    S+=i
print('YES' if S%2==0 else 'NO')