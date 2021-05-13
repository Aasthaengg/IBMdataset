#!/user/bin/env pypy3
import itertools
import sys


def fast_input():
    return sys.stdin.readline()[:-1]


def print_format(b: bool) -> str:
    return "YES" if b else "NO"


def solve(s: str) -> bool:
    for p in itertools.permutations(["dreamer", "eraser", "dream", "erase"]):
        work = s
        for token in p:
            work = work.replace(token, '')
        if work == "":
            return True
    return False


def main():
    result = solve(fast_input())
    print(print_format(result))


main()
