N = int(input())
A = [int(x) for x in input().split()]
#a, b, c = map(int, input().split())
#name1 = str(input())
#alph = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
for i in range(N):
    A[i] = A[i] - (i + 1)
A.sort()
b = A[int(N / 2)]
ans = 0
for i in range(N):
    ans += abs(A[i] - b)
print(ans)
