A,B,C=map(int, input().split())
K=int(input())
a=max(A,B,C)
b=A+B+C-a
print(b+a*(2**K))