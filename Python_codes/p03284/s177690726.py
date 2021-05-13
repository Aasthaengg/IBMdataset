N, K = map(int, input().split(" "))

q, r = divmod(N, K)
if r == 0:
    print(0)
else:
    print(1)
