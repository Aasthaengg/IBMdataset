a, b, k = map(int, input().split())

def it():
    for i in range(a, min(a+k, b)):
        yield i

    for i in range(max(b-k+1, a), b+1):
        yield i

for i in sorted(set(it())):
    print(i)