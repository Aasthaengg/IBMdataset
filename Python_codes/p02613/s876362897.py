import sys
import numpy as np  # noqa

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(readline())

AC, WA, TLE, RE = 0, 0, 0, 0

for i in range(N):
    s = readline().rstrip().decode()
    if s == "AC":
        AC += 1
    elif s == "WA":
        WA += 1
    elif s == "TLE":
        TLE += 1
    elif s == "RE":
        RE += 1

print(f"AC x {AC}")
print(f"WA x {WA}")
print(f"TLE x {TLE}")
print(f"RE x {RE}")
