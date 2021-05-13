import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    N = int(input())
    for h in range(1, 3501):
        for n in range(1, 3501):
            shisu = h * N * n
            bosu = n * (h * 4 - N) - h * N
            if bosu >= 1:
                if not (shisu / bosu) % 1:
                    print(h, n , int((h * N * n) / (n * (h * 4 - N) - h * N)))
                    sys.exit()

if __name__ == '__main__':
    main()