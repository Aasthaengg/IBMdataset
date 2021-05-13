N = int(input())

A = map(int,input().split())



li = [[0]*N,[0]*N ]

for index,a in enumerate(A):
    li[0][index] = a- index
    li[1][index]= -a - index


from collections import Counter


cou_one = Counter(li[0])
cou_two = Counter(li[1])




counter = 0
for key,value in cou_one.items():
    counter += cou_two[key]*value


print(counter)