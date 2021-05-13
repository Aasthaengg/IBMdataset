import statistics
A = list(map(int, input().split()))
B = statistics.mode(A)
[print(i) for i in A if i != B]