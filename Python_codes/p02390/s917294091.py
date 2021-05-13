t = input()
t = int(t)

s = t % 60
t //= 60
m = t % 60
t //= 60
h = t

print("{0}:{1}:{2}".format(h, m, s))