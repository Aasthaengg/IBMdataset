def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

X, A = MI()

print(0 if X < A else 10)