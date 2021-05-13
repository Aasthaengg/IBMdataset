class Work:
    require = 0
    limit = 0
    def __init__(self, require, limit) -> None:
        self.require = require
        self.limit = limit

def from_list(xs) -> Work: 
    return Work(xs[0], xs[1])

N = int(input())

works = [from_list([int(_) for _ in input().split()]) for i in range(N)]

def solve(works):
    works.sort(key=lambda x: x.limit)
    acc = 0
    for w in works:
        acc += w.require
        if acc > w.limit:
            return "No"
    return "Yes"

print(solve(works))