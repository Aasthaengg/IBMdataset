a, b, c = map(int, input().split())
k = int(input())
abc = [a, b, c]
abc.sort()
for _ in range(k):
    abc[-1] *= 2
print(sum(abc))