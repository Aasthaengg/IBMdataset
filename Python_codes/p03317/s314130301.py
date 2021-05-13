Len, Split = map(int, input().split())
_res = (Len - 1) % (Split - 1)
if _res:
    res = int(((Len - 1) // (Split - 1)) + 1)
    print(res)
else:
    res = int((Len - 1) // (Split - 1))
    print(res)