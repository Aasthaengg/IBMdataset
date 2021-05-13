_ = input()
a = [int(i) for i in input().split()]
a.sort()
a.reverse()
print(sum(a[::2]) - sum(a[1::2]))