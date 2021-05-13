N = int(input())
d = list(map(int, input().split()))
d.sort()
middle = (N // 2) -1
print(d[middle+1] - d[middle])