n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse = True)

length = sum(l[0 : k])

print(length)