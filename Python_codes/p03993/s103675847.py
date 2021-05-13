N = int(input())
A = [int(a) - 1 for a in input().split()]
liked = [set() for _ in range(N)]
for i in range(N):
    liked[A[i]].add(i)

count = 0
for i in range(N):
    if A[i] in liked[i]:
        count += 1

print(count // 2)