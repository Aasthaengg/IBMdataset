import sys

input = sys.stdin.readline



d, t, s= map(int, input().split())

time = d / s

if time <= t:
    print("Yes")
else:
    print("No")