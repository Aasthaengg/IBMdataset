def inpl(): return list(map(int, input().split()))
A, B = inpl()
print(max([A+B, A-B, A*B]))