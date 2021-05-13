abc = sorted(list(map(int, input().split())))
k = int(input())

for i in range(k):
    abc[2] *= 2

print(sum(abc))