import sys
def main():
    for line in sys.stdin:
        m, f, r = map(int, line.split())
        if m == -1 and f == -1 and r == -1:
            break
        else:
            total = m + f
            if m == -1 or f == -1:
                print("F")
            elif total >= 80:
                print("A")
            elif 65 <= total < 80:
                print("B")
            elif 50 <= total < 65:
                print("C")
            elif 30 <= total < 50:
                if r >= 50:
                    print("C")
                else:
                    print("D")
            elif total < 30:
                print("F")


if __name__ == "__main__":
    main()