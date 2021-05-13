n = int(input())
a = [int(s) for s in input().split()]
if sum(a) % 2 == 0:print("YES")
else:print("NO")