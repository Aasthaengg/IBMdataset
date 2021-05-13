n = int(input())
a = list(map(int, input().split()))
k = 0
for x in a:
    k ^= x
for x in a:
    print(k ^ x, end=" ")
print()