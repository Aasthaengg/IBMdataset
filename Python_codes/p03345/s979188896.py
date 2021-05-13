A,B,C,K = map(int,input().split())
for i in range(K%2):
    A,B,C = B+C,C+A,A+B
print(A-B)