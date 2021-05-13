import itertools
N = input().split()
for x in itertools.permutations(N):
    num = int("".join(x))
    if num == 1974:
        print("YES")
        exit()
print("NO")
