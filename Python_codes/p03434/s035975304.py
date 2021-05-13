n = int(input())
a = sorted((map(int, input().split())))
a.reverse()
print(sum(a[0::2]) - sum(a[1::2]))