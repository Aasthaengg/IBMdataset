from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

s = input() + "T"
x, y = map(int, input().split())

stepx = []
stepy = []

headx = True
step = 0
for c in s:
    if c == "F":
        step += 1
    else:
        if headx:
            stepx.append(step)
        else:
            stepy.append(step)
        headx = not headx
        step = 0

x -= stepx[0]
stepx = stepx[1:]


class Reachable:
    def __init__(self, steps):
        self.steps = steps

        self.maxs = sum(steps)
        self.r = [{} for _ in range(len(steps))]

    def __call__(self, i, s):
        if i == -1:
            return s == 0
        elif not -self.maxs <= s <= self.maxs:
            return False
        elif self.r[i].get(s, None) is not None:
            return self.r[i][s]
        else:
            step = self.steps[i]
            r = self(i - 1, s - step) or self(i - 1, s + step)
            self.r[i][s] = r
            return r


answer = Reachable(stepx)(len(stepx) - 1, x) and Reachable(stepy)(len(stepy) - 1, y)

if answer:
    print("Yes")
else:
    print("No")
