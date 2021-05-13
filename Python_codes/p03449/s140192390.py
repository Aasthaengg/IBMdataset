# AtCoder Beginner Contest 087
# C - Candies

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

p=[]

for i in range (N):
    tempA=A[:1+i]
    tempB=B[0+i:]
    # print(tempA,tempB)
    p.append(sum(tempA)+sum(tempB))

print(max(p))