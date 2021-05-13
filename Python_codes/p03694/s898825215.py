N=int(input())
a=[int(x) for x in input().rstrip().split()]
a.sort()

print(max(a)-min(a))