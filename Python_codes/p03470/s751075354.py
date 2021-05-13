N=int(input())
d=[]
for i in range(N):
    d.append(int(input()))
e=list(set(d))
print(len(e))