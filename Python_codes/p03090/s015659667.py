from itertools import combinations
n=int(input())
A=[]
num=n if n%2==1 else n+1
for a,b in combinations([j+1 for j in range(n)],2):
    if a+b!=num:A.append([a,b])
print(len(A))
for i in A:print(*i)