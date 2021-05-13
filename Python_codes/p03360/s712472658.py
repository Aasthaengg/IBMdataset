l = list(map(int,input().split()))
k = int(input())
for i in range(k):
    l[l.index(max(l))] *= 2
print(sum(l))