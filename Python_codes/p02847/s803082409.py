import sys
input = sys.stdin.readline

day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

s = input()[:-1]

print(7-day.index(s))