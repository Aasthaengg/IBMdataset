n,k=map(int, input().split())
l=list(range(1,n+1))
for i in range(k):
    d = int(input())
    a = [int(x) for x in input().split()]
    for k in range(len(a)):
        if a[k] in l:
            l.remove(a[k])
            
print(len(l))