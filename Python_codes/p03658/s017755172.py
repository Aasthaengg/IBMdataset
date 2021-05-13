n,k = map(int,input().split())
l = list(map(int,input().split()))
list.sort(l,reverse = True)
c = 0

for i in range(k):
    c = c + l[i]

print(c)