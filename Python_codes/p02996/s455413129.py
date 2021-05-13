N = int(input())

Works = [dict(zip(["require", "limit"], [int(_) for _ in input().split()])) for i in range(N)]

def solve(Works):
    Works.sort(key=lambda x: x["limit"])
    acc = 0
    for w in Works:
        acc += w["require"]
        if acc > w["limit"]:
            return "No"
    return "Yes"

print(solve(Works))