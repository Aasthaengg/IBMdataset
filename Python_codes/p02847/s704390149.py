import sys
input = lambda : sys.stdin.readline().rstrip()
mod = 10**9 + 7

days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
d = {}
for i in range(7):
    d[days[i]] = 7 - i
s = input()
print(d[s])