n=int(input())
p=[]
for i in range(n):
    p.append(int(input()))
p.append(p.pop(p.index(max(p)))//2)
print(sum(p))
