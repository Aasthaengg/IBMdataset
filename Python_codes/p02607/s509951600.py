n = int(input())
a = [int(i) for i in input().split()]
print(sum(ai % 2 == 1 for ai in a[::2]))