from collections import defaultdict
N=int(input())
A=list(map(int,input().split()))

dic=defaultdict(int)
result=0
posi=0

for i in range(N):
    dic[A[i]-(i+1)] +=1

sort_dic=sorted(dic.items())

for j in sort_dic:
    if posi+j[1]>N//2:
        siki=j[0]
        break
    else:
        posi+=j[1]

for k in sort_dic:
    result+=abs(k[0]-siki)*k[1]

print(result)