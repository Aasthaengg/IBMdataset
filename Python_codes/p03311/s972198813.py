N = int(input())
A = list(map(int, input().split()))

A_diff = []
for i, a in enumerate(A):
    A_diff.append(a - (i + 1))
    

A_diff.sort()
A_diff.reverse()

print(sum(list(map(lambda x : abs(x - A_diff[N//2]), A_diff))))