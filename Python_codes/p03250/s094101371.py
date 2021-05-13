A,B,C=map(int,input().split())
n=max(10*A+B+C,A+10*B+C,A+B+10*C)
print(n)