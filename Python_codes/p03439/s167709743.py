N = int(input())


def question(i):
    print(i)
    s = input()
    if s == 'Male':
        return 0
    elif s == 'Female':
        return 1
    exit()


a = question(0)
A = ([a, 1 - a] * N)[:N]
lb = -1
rb = N
while True:
    mid = (lb + rb) // 2
    if question(mid) == A[mid]:
        lb = mid
    else:
        rb = mid
