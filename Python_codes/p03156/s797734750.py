n = int(input())
a, b = map(int, input().split())
p = map(int, input().split())
problems = [0] * 3
for pi in p:
    if pi <= a:
        problems[0] += 1
    elif pi <= b:
        problems[1] += 1
    else:
        problems[2] += 1
print(min(problems))
