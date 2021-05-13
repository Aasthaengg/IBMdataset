n = int(input())
A = sorted(list(map(int, input().split())))[::-1]
print(sum(a for a in A[1:2*n:2]))