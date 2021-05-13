n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort()
l[-1]=l[-1]//2
print(sum(l))
