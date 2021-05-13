
n = int(input())

R = []

for i in range(n):
    R.append(int(input()))

kouho = set()
diff_max = None

for (i, rt) in enumerate(R):
    if i == 0:
        rt_min = rt
    else:
        if rt < rt_min and not (diff_max is None):
            kouho.add(diff_max)
            diff_max = None
            rt_min = rt
        elif rt < rt_min and diff_max is None:
            rt_min = rt
        elif rt >= rt_min:
            if diff_max is None:
                diff_max = rt - rt_min
            else:
                diff_max = max(diff_max, rt - rt_min)

if not (diff_max is None):
    kouho.add(diff_max)

# print(kouho)

if kouho != set():
    print(max(kouho))
else:
    diff_tonari = {R[i + 1] - R[i] for i in range(n - 1)}
    print(max(diff_tonari))