N = int(input())
a = sorted([int(i) for i in input().rstrip().split(' ')])
print(sum(a[N::2]))