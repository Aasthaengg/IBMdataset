#!/usr/bin/env python3

wd = "SUN MON TUE WED THU FRI SAT".split()
wd = list(reversed(wd))

def solve(S: str):
    idx = wd.index(S)
    return idx+1


def main():
    S = input().strip()
    answer = solve(S)
    print(answer)

if __name__ == '__main__':
    main()
