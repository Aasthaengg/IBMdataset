import math
def main():
    d = int(input())
    th = 90

    eps = 10**(-12)
    x = y = ans = 0
    while True:
        x += math.cos(math.radians(th))
        y += math.sin(math.radians(th))
        ans += 1

        if abs(x) <= eps and abs(y) <= eps:
            print(ans)
            break
        else:
            th += d

if __name__ == "__main__":
    main()