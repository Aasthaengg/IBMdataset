h, n = (int(n) for n in input().split())
list_a = [int(n) for n in input().split()]
if h <= sum(list_a): print("Yes")
else: print("No")