n=int(input())
s=[]
for i in range(n):
    p=int(input())
    s.append(p)
print(sum(s)-max(s)//2)
