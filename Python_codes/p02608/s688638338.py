import math


def main():
    N = int(input())
    sqrt = int(math.sqrt(N))
    ans = [0] * (N+1)
    for x in range(1, sqrt+1):
        for y in range(1, sqrt+1):
            for z in range(1, sqrt+1):
                tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if tmp <= N:
                    ans[tmp] += 1
    for i in range(1, N+1):
        print(ans[i])


if __name__ == "__main__":
    main()
