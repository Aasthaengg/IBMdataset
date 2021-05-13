def main():
    n = int(input())
    d = dict()
    for i in range(1, 10001):
        d[i] = 0
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                r = x**2+y**2+z**2+x*y+y*z+z*x
                if r <= 10000:
                    d[r] += 1
    for i in range(1, n+1):
        print(d[i])


main()
