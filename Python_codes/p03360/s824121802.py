A,B,C=map(int,input().split())
K=int(input())
summy=((2**K)*(max(A,B,C)))+A+B+C-max(A,B,C)
print(summy)