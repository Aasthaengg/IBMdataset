s = input()
c_index = float('inf')
f_index = 0
for i, c in enumerate(s):
    if c == "C":
        c_index = min(c_index, i)
    if c == "F":
        f_index = max(f_index, i)
if c_index < f_index:
    print("Yes")
else:
    print("No")
