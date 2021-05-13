# import math
# import statistics
# import itertools
# a=int(input())
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
A,B,C= map(int,input().split())
# f = list(map(int,input().split()))
# g = [int(input()) for _ in range(N)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

nowA=A
nowB=B
nowC=C
count=0
if A%2==1 or B%2==1 or C%2==1:
    print(0)
elif A==B==C :
    print(-1)
else:
    while True:
        nowA=B//2+C//2
        nowB=A//2+C//2
        nowC=A//2+B//2
        A=nowA
        B=nowB
        C=nowC
        count+=1
        if nowA%2==1 or nowB%2==1 or nowC%2==1:
            print(count)
            exit()
