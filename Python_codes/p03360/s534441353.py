abc = list(map(int, input().split()))
k = int(input())
for i in range(k):
    abc.sort()
    abc[-1] *= 2
print(sum(abc))
