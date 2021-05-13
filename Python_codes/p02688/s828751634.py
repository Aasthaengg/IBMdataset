n,k=map(int,input().split())
l=[]

for i in range(k):
    d = int(input())
    l+=map(int,input().split())
print(n-int(len(set(l))))