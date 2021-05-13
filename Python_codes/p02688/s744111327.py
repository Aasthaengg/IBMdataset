n,k = map(int,input().split())

candy_set = set()
for i in range(k):
    d = int(input())
    snuke = list(map(int,input().split()))
    for s in snuke:
        candy_set.add(s)

count = 0
for i in range(n):
    if not i+1 in candy_set:
        count+=1
print(count)