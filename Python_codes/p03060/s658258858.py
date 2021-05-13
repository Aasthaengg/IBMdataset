import itertools

N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
temp = itertools.product([0, 1], repeat=N)
ans = 0
for T in temp:
    an = 0
    for i, e in enumerate(T):
        if e == 1:
            an += V[i] - C[i]
    ans = max(ans,an)
print(ans)
