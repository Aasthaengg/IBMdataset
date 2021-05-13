import numpy as np
import math as m

def main(**kwargs):
    A = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

    res = A[k-1]
    return res

if __name__ == "__main__":
    cin = np.array(input().split(" ")).astype("int")
    k, *_ = cin

    cout = main(k=k)
    print(cout)