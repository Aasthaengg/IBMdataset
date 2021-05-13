s = input()
t = ['A', 'C', 'G', 'T']
mx = 0
a = 0
for ss in s:
    if ss in t:
        a += 1
    else:
        mx = max(mx, a)
        a = 0
mx = max(mx, a)
print(mx)
