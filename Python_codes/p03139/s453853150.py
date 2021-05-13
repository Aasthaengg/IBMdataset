N, A, B = map(int, input().split())

ans1 = B if A>B else A
ans2 = A+B-N if A+B-N >= 0 else 0

print("{} {}".format(ans1, ans2))