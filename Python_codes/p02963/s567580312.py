S = int(input())
ans = [0, 0, 1, 10 ** 9]
if S % (10 ** 9) == 0:
    ans.extend([S // (10 ** 9), 0])
else:
    ans.extend([S // (10 ** 9) + 1, 10 ** 9 - S % (10 ** 9)])
print(' '.join([str(a) for a in ans]))