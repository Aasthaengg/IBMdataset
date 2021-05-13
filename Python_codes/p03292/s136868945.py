import sys
import math
import bisect

def main():
    A = list(map(int, input().split()))
    B = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if j != i and k != i and k != j:
                    val = abs(A[j] - A[i]) + abs(A[k] - A[j])
                    B.append(val)
    print(min(B))

if __name__ == "__main__":
    main()
