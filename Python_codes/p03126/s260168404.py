n, m = map(int,input().split())
lst = []
for _ in range(n):
    l = list(map(int, input().split()))
    lst.append(l[1:])

ansset = set(lst[0])
for i in range(1,n):
    ansset = ansset & set(lst[i])

print(len(ansset))
