import numpy as np


def main():
    a, b = map(int, input().split())
    x = np.mean([a, b])
    ans = int(np.ceil(x))
    print(ans)


if __name__ == "__main__":
    main()
