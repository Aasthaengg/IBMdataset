n = int(input())
dlst = list(map(int, input().split()))
dlst.sort()
abc_max = dlst[n // 2 - 1]
arc_min = dlst[n // 2]
print(arc_min - abc_max)