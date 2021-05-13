import math
N=int(input())
A=[]
B=[]
for _ in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
answer=0
A.reverse()
B.reverse()
number=0
for a in A:
    a+=answer
    answer+=math.ceil(a/B[number])*B[number]-a
    number+=1
print(answer)
