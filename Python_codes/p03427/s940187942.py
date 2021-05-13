N = input()

f = int(N[0])
res = (len(N) - 1) * 9 + f - 1
s = 0
for i in N:
    s += int(i)

print(max(res, s))
