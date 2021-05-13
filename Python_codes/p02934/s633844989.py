N=int(input())
S=0
A=list(map(int,input().split()))
for i in A:S+=1/i
print(1/S)