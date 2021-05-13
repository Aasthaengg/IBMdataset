N = int(input())
a = list(map(int, input().split()))
ave = sum(a) / len(a)
result = -1
tmp = float('inf')
for i, ai in enumerate(a):
    if tmp > abs(ai - ave):
        tmp = abs(ai - ave)
        result = i
print(result)
