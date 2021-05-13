n,k,q = map(int,input().split())
lst = [None] + [0 for _ in range(n)]

for _ in range(q):
    a = int(input())
    lst[a] += 1

for x in lst[1:]:
    if x > q-k:
        print("Yes")
    else:
        print("No")