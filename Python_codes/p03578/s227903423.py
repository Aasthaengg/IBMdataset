from collections import defaultdict
D=defaultdict(int)
E=defaultdict(int)
n=int(input())
l=map(int,input().split())
for i in l:
    D[i]+=1
m=int(input())
e=map(int,input().split())
for j in e:
    E[j]+=1
for i in E.keys():
    if E[i]>D[i]:print("NO");exit()
print("YES")