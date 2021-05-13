N = int(input())
A, B = map(int, input().split())

c = [0] * 3
for P in map(int, input().split()):
    if P <= A:
        c[0] += 1
    elif A < P <= B:
        c[1] += 1
    else:
        c[2] += 1

print(min(c))