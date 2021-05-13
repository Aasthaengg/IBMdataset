from sys import stdin

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

S = int(stdin.readline().rstrip())

h, m = divmod(S, SECONDS_PER_HOUR)
m, s = divmod(m, SECONDS_PER_MINUTE)

print("{}:{}:{}".format(h, m, s))

