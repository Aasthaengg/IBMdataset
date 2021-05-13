def is_ok(val, N, d):
    if val < 0:
       return True
    val_s = str(val)
    if len(val_s) != N:
        return False
    for s, c in d.items():
        # print("val_s = {}, s = {}, c = {}".format(val_s, s, c))
        if int(val_s[s-1]) != c:
            return False
    return True

N, M = map(int, input().split())

d = {}
flag = True

for i in range(M):
    s, c = map(int, input().split())
    if s in d.keys() and d[s] != c:
        print("-1")
        exit()
    d[s] = c

# res = binary_search(N, d, -1, 10 ** 4, is_ok)

for i in range(0, 10 ** 4):
    if is_ok(i, N, d):
        print(i)
        exit()

print("-1")