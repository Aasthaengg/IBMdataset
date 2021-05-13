n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
L=sorted(l)
print(sum(L[:-1])+L[-1]//2)