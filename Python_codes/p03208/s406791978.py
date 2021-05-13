N,K=map(int,input().split())
s=0
l=[]
L=[]
for i in range(N):
    h=int(input())
    l.append(h)
l=sorted(l)
for j in range(N-(K-1)):
    L.append(l[j+(K-1)]-l[j])
print(min(L))