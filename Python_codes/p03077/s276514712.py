import math


def main():
    n = int(input())
    csr = []
    for _ in range(5):
        csr.append(int(input()))
    # print(5+n//min(csr))
    print(4+math.ceil(n/min(csr)))


if __name__ == "__main__":
    main()
