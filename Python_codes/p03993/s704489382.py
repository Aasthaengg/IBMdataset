from collections import Counter

n = map(int, input().split())

A = list(map(int, input().split()))

def f(): 
    for i, a in enumerate(A, 1):
        if i < a:
            yield i, a
        else:
            yield a, i

c = Counter(f())
print(len([k for k, v in c.items() if v == 2]))