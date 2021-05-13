A,B,K=map(int,input().split())

for i in range(K):
    if not i%2:
        A=A-A%2
        A,B=A//2,B+A//2
    else:
        B=B-B%2
        A,B=A+B//2,B//2
print(A,B)