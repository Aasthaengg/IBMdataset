n=int(input())
a=[]
for i in range(n):
   a.append(input().strip())
print(len(list(set(a))))