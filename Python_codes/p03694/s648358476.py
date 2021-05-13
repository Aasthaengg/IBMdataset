N = int(input())
a = list(map(int,(input().split())))
a.sort()
print(max(a)-min(a))