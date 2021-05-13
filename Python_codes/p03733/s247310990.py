N, T = map(int, input().split())

ts = list(map(int, input().split()))

def it():
    for i in range(N-1):
        diff = ts[i+1] - ts[i]
        if diff <= T:
            yield diff
        else:
            yield T
    yield T

print(sum(it()))






