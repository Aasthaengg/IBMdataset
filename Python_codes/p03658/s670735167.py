n, k = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)
length = 0
for i in range(k):
    length += l[i]
print(length)