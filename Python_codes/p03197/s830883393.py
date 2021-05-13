import numpy as np

def main():
    stdin = np.fromstring(open(0).read(), dtype=np.int32, sep=' ')
    N = stdin[0]
    A = stdin[1:]
    A = np.mod(A, 2)
    print("first") if np.count_nonzero(A) else print("second")
if __name__ == "__main__":
    main()