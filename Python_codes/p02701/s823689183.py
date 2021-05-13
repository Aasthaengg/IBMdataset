n=int(input())
ans=0
s=[]
for i in range(n):
    s.append(str(input()))
s=set(s)
print(len(s))