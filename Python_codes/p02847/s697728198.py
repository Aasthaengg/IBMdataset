S = input()
W = ["SAT","FRI","THU","WED","TUE","MON","SUN"]
p = 0
for i in range(7):
    p += 1
    if S == W[i]:
        break
print(p)
