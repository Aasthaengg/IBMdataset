N = int(input())
B = list(map(int, input().split()))
A = [B[0], B[0]]

for b in B[1:]:
    if A[-1] <= b:
        A += [b]
    else:
        A[-1] = b
        A += [b]
# print(f"A:{A}", file=sys.stderr)
print(sum(A))    