n = int(input())
list_a = sorted((int(n) for n in input().split()))
print(list_a[-1] - list_a[0])