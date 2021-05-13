A,B,C=map(int,input().split())
K=int(input())
print(A+B+C-max(A,max(B,C))+max(A,max(B,C))*2**K)