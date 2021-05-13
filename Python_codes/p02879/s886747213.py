A, B = map(int, input().split())

ok = 1 <= A <= 9
ok = ok and (1 <= B <= 9)

print(A * B if ok else -1)