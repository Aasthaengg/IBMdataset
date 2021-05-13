# import math
# import statistics
#a=input()
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#    c.append(i)
e1,e2,e3 ,e4= map(int,input().split())
#K = input()
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]

if e4%2==0 or e4==0:
    print(e1-e2)
elif e4%2==1 :
    print(-(e1-e2))
elif abs(e1-e2)>=10**18:
    print("Unfair")