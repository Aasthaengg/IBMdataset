# import math
# import statistics
# import itertools
a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
#e1,e2= map(int,input().split())
# f = list(map(int,input().split()))
#g = [input() for _ in range(e1)]
n=1
while True:
    if 360*n%a==0:
        print(360*n//a)
        exit()
    else:
        n+=1


