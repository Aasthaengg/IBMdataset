from itertools import permutations

n = list(map(int, input().split()))
for a in permutations(n):
    if a == (1, 9, 7, 4):
        print("YES")
        exit()
print("NO")
