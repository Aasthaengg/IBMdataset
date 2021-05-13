n=int(input())
l=[]
for _ in range(n):
    k=int(input())
    if k not in l:l.append(k)
print(len(l))