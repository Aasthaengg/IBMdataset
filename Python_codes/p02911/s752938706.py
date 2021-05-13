n, k, q = map(int,input().split())
lst = [0 for i in range(n)]
for i in range(q):
    a = int(input())
    lst[a - 1] = lst[a - 1] + 1

for i in range(n):
    lst[i] = k - (q - lst[i])

for i in range(n):
    if (lst[i] > 0):
        print("Yes")
    else:
        print("No")
