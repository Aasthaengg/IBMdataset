import random
D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in [0]*D]
for i in range(D):
    print(random.randint(1,26))