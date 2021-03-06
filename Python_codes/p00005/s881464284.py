def main():
    while True:
        try:
            a, b = map(int, input().split())
            
            gcd = rec(a, b)
            lcm = a * b / gcd

            print(gcd, int(lcm))
        except:
            break

def rec(i, j):
    if i % j == 0:
        return j
    return rec(j, i % j)

if __name__ == '__main__':
    main()