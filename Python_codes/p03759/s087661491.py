t = list(map(int, input().rstrip().split()))

print('YES' if (t[1] - t[0] == t[2] - t[1]) else 'NO')
