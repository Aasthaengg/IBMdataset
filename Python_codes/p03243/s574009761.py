def not_xxx(N):
    X = list(str(N))
    if len(set(X)) == 1:
        return False
    else:
        return True

N = int(input())

while not_xxx(N):
    N += 1

print(N)
