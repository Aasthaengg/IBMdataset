n = int(input())
if n == 1:
    print('Yes')
    print(2)
    print("1 1")
    print("1 1")
    exit()
t = [3]
cnt = 3
while t[-1]+cnt <= n:
    t.append(t[-1]+cnt)
    cnt += 1
if t[-1] != n:
    print('No')
    exit()
print('Yes')
try:
    n_cols = t[-1]-t[-2]
except:
    print(3)
    print("2 1 2")
    print("2 3 1")
    print("2 2 3")
    exit()
print(n_cols+1)
t_len = len(t)
t2 = [i+1 for i in t]
t3 = [0 for i in t]
for col in range(n_cols+1):
    out = str(n_cols)
    if col <=2:
        if col == 0:
            out += " 1 2"
        elif col == 1:
            out += " 1 3"
        elif col == 2:
            out += " 2 3"
    else:
        idx = t[col-3]+1
        while idx <= t[col-2]:
            out += " " + str(idx)
            idx += 1
    for i in range(t_len-1):
        if t2[i] != t[i+1]+1:
            out += " " + str(t2[i])
            t2[i] += 1
    print(out)