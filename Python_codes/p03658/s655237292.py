n,k = map(int,input().split())
li = list(map(int,input().split()))
lia = sorted(li, reverse=True)
a = 0
for i in range(k):
    a += lia[i]
print(a)