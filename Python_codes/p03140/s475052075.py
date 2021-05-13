import math
# a=int(input())
b=int(input())
# c=[]
# for i in b:
#     c.append(i)
#e = list(map(int,input().split()))
#f = list(map(int,input().split()))
j = [input() for _ in range(3)]
a1=[i for i in j[0]]
a2=[i for i in j[1]]
a3=[i for i in j[2]]

count=0

for i in range(b):
    if a1[i]==a2[i]==a3[i]:
        count+=0
    elif a1[i]==a2[i] or a1[i]==a3[i] or a2[i]==a3[i]:
        count+=1
    else:
        count+=2

print(count)