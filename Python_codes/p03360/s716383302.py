a, b, c = map(int, input().split())
k = int(input())

l = [a, b, c]
l.sort(reverse=True)
for x in range(k):
    l[0] *= 2

print(sum(l))
