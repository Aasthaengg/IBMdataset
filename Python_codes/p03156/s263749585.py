n = int(input())
a, b = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
key1 = 0
key2 = n-1
for i in range(n):
    if p[i] > a:
        key1 = i-1
        break
for i in range(key1+1,n):
    if p[i] > b:
        key2 = i-1
        break
print(min(key1+1,key2-key1,len(p)-1-key2))