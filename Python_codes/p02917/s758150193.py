N = int(input())
B = [10**6] + list(map(int, input().split())) + [10**6]
print(sum([min(b1, b2) for b1, b2 in zip(B[:-1], B[1:])]))
