n = int(input())
A = list(map(int, input().split()))
A_r = [1/a for a in A]
print(1/sum(A_r))