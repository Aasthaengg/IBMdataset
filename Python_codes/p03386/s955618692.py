A,B,K = map(int, input().split())
[print(i) for i in sorted(list(set([i for i in range(A,A+K)] + [i for i in reversed(range(B-K+1, B+1))]))) if A <= i <= B]
