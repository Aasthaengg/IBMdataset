n,k = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*(n+1)
for x in a:
    b[x]+=1
b.sort(reverse=1)
print(sum(b[k:]))



