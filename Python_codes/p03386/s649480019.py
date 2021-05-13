import sys
input = sys.stdin.readline

A,B,K = list(map(int,input().split()))
num_lis = []
for i in range(A,A+K):
    if i <= B:
        num_lis.append(i)
    else:
        break
    
for i in range(B,B-K,-1):
    if i>= A:
        num_lis.append(i)
    else:
        break
b = sorted(list(set(num_lis)))

for i in range(len(b)):
    print(b[i])
