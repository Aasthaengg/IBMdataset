import math


def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    l = [n, 0, 0, 0, 0, 0]
    time = 0

    move_a = a
    move_b = min(move_a, b)
    move_c = min(move_b, c)
    move_d = min(move_c, d)
    move_e = min(move_d, e)

    time = math.ceil(n / move_e) + 4

    print(time)


'''
    while True:
        move_a = min(a, l[0])
        move_b = min(b, l[1])
        move_c = min(c, l[2])
        move_d = min(c, l[3])
        move_e = min(c, l[4])

        l[0] -= move_a
        l[1] += move_a
        l[1] -= move_b
        l[2] += move_b
        l[2] -= move_c
        l[3] += move_c
        l[3] -= move_d
        l[4] += move_d
        l[4] -= move_e
        l[5] += move_e

        time += 1
        if l[5] >= n:
            break

    print(time)
'''

'''
    0: [n-a, a, 0, 0, 0, 0]
    1: [n-2a,2a-b, b, 0, 0, 0]
    2: [n-3a,3a-2b, 2b-c, c, 0, 0]
    3: [n-4a, 4a-3b, 3b-2c, 2c-d, d, 0]
    4: [n-5a, 5a-4b, 4b-3c, 3c-2d, 2d-e, e]
    5: [n-6a, 6a-5b, 5b-4c, 4c-3d, 3d-2e, 2e]
    6: [n-7a, 7a-5b, 6b-5c, 5c-4d, 4d-3e, 3e]

    v1: 全員が0->1に移動する: math.ceil(n/a)
    v2: 全員が1->2に移動する: math.ceil(n/min(v1, b))
    v3: 2->3: math.ceil

'''


if __name__ == "__main__":
    main()
