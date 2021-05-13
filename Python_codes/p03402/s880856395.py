# dame datta...
def main():
    A, B = map(int, input().split())
    t = [[0] * 100 for _ in range(50)] + [[1] * 100 for _ in range(50)]
    x = 0
    b = False
    for i in range(0, 50, 2):
        for j in range(0, 100, 2):
            if x == A - 1:
                b = True
                break
            t[i][j] = 1
            x += 1
        if b:
            break
    x = 0
    b = False
    for i in range(51, 100, 2):
        for j in range(0, 100, 2):
            if x == B - 1:
                b = True
                break
            t[i][j] = 0
            x += 1
        if b:
            break
    print(100,100)
    for i in range(100):
        print(''.join('.' if i == 1 else '#' for i in t[i]))
main()
