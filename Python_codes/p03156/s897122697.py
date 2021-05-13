N = int(input())
A, B = map(int, input().split())
first = 0
second = 0
third = 0
for P in input().split():
    P = int(P)
    if P <= A:
        first += 1
    elif P <= B:
        second += 1
    else:
        third += 1
print(min(first, second, third))
