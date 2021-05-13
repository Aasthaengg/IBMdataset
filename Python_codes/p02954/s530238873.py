#create date: 2020-07-05 18:05

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    s = ns()
    l = False
    ans = [0] * len(s)
    z = [0, 0]
    for i, si in enumerate(s):

        if si =="L" and not l:
            rl = i
            l = True
        if si == "R" and l:
            if rl % 2 == 0:
                ans[rl-1] = z[1]
                ans[rl] = z[0]
            else:
                ans[rl-1] = z[0]
                ans[rl] = z[1]
            l = False
            z = [0, 0]
        if i % 2 == 0:
            z[0] += 1
        else:
            z[1] += 1
    if rl % 2 == 0:
        ans[rl-1] = z[1]
        ans[rl] = z[0]
    else:
        ans[rl-1] = z[0]
        ans[rl] = z[1]
    print(*ans)
        


if __name__ == "__main__":
    main()