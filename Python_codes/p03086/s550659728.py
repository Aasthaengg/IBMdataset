items = ['A', 'C', 'G', 'T']

def chkmax(a, b):
    return a if a > b else b

res = 0
cnt = 0
for c in list(input()):
    if c in items:
        cnt += 1
        res = chkmax(res, cnt)
    else:
        cnt = 0
print(res)

