N=int(input())
A=list(map(int,input().split()))
ev = sum([1 for a in A if a%2==0])
print(pow(3,N)-pow(2,ev))