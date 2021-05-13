N = int(input())
A = [int(x) for x in input().split()]

nodd = sum(a % 2 for a in A)
if nodd % 2 == 0:
    print("YES")
else:
    print("NO")