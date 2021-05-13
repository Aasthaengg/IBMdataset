N, K = list(map(int, input().strip().split()))
ls = list(map(int, input().strip().split()))

ls = sorted(ls, reverse = True)
print(sum(ls[:K]))