from sys import stdin


def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]


def fetch_int_inputs(times):
    return [[int(s) for s in fetch_one_line()] for _ in range(times)]


answers = "Left Balanced Right".split()
A, B, C, D = fetch_int_input()

left = A + B
right = C + D
if left > right:
    id = 0
elif left < right:
    id = 2
else:
    id = 1

print(answers[id])
