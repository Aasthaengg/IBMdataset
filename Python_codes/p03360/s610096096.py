abc = list(map(int, input().split()))
k = int(input())

abc = sorted(abc)
for i in range(k):
    abc[-1] = abc[-1]*2

print(sum(abc))
