def is_kaibun(n):
    ns = [int(v) for v in str(n)]

    i = 0
    j = len(ns) - 1
    while i < j:
        if ns[i] != ns[j]:
            return False
        i += 1
        j -= 1

    return True


A, B = map(int, input().split())

count = 0
for i in range(A, B + 1):
    if is_kaibun(i):
        count += 1

print(count)
