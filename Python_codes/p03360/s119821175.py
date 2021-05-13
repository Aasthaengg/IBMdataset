l = list(map(int, input().split()))
k = int(input())
for i in range(k):
    l = sorted(l)
    l[2] *= 2
print(sum(l))