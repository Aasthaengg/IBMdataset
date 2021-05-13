input()
(*v,) = sorted(map(int, input().split()), reverse=True)
v[-1] *= 2
print(sum((a / (2 ** i)) for i, a in enumerate(v, start=1)))