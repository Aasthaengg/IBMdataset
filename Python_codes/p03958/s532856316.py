K, T = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort(reverse=True)

# スペース
space = A[0] - 1
for x in A[1:]:
    space -= x

print(max(0, space))