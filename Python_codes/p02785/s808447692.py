n, k = map(int, input().split())
hlst = list(map(int, input().split()))
if k >= n:
    print(0)
else:
    hlst.sort(reverse = True)
    print(sum(hlst[k:]))