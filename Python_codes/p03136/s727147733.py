n = int(input())
list_l = sorted([int(n) for n in input().split()])
if sum(list_l[:n - 1]) > list_l[n - 1]: print("Yes")
else: print("No")