n, a, b = map(int, input().split())
ans1 = min([a, b])
ans2 = max([0, a+b-n])
print('{} {}'.format(ans1, ans2))