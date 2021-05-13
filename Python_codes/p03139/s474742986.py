N, A, B = map(int, input().split())
ans1 = min(A, B)
ans2 = max(A + B - N, 0)
print("{} {}".format(ans1, ans2))
