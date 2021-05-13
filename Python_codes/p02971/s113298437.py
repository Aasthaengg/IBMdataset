n = int(input())
lst = [int(input()) for _ in range(n)]

lst2 = sorted(lst)
saidai = max(lst2)

for i in range(n):
    if lst[i] != saidai:
        print(lst2[-1])
    else:
        print(lst2[-2])