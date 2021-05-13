N=int(input())
B=list(map(int,input().split()))
B.append(B[-1])
A=[B[0]]
for i in range(len(B)-1):
    A.append(min(B[i],B[i+1]))
print(sum(A))