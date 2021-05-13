from collections import Counter
s = input()
x = Counter(s)
y = sorted(list(x.values()))
if y[0]*y[-1] == 4:
    print("Yes")
else:
    print("No")