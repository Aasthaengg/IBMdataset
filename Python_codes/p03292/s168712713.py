import itertools
a = [int(i) for i in  input().split()]

def cost(a):
    return abs(a[0]-a[1])+abs(a[1]-a[2])

ans = sum(a)
for i in itertools.permutations(a):
    c = cost(i)
    if c < ans:
        ans = c

print(ans)
