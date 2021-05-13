def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

SIZE = 3501

def main():
    N = Z()
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            x = N * i * j
            y = 4*i*j - N * (i+j)
            if y > 0 and x%y == 0:
                print(i, j, x//y)
                break
        else: continue
        break

    return

if __name__ == '__main__':
    main()

