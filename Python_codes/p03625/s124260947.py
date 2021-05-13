n = int(input())
seq = sorted((int(x) for x in input().split()), reverse=True)
val1 = None
val2 = None
cur_val = seq[0]
for val in seq[1:]:
    if val == cur_val:
        if val1 is None:
            val1 = val
            cur_val = None
        elif val2 is None:
            val2 = val
            break
    else:
        cur_val = val
if val1 is None or val2 is None:
    print(0)
else:
    print(val1 * val2)
