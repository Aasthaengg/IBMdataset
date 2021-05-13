s = int(input())

h = int(s / (60 * 60))
m = int((s % (60 * 60)) / 60)
s = int(s % 60)

print(h, m, s, sep = ":")