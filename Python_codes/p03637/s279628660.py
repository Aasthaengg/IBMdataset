N = int(input())

ARR = [int(s) for s in input().split(" ")]
def calculate(n,arr):
    m1 = 0
    m2 = 0
    m3 = 0
    for ar in arr:
        if ar % 4 == 0:
            m1 = m1 + 1
        elif ar % 2 == 0:
            m2 = m2 + 1
        else:
            m3 = m3 + 1

    if m2 == 0:
        if m3 > m1 + 1:
            print("No")
        else:
            print("Yes")
    else:
        if m3 <= m1:
            print("Yes")
        else:
            print("No")


calculate(N,ARR)
