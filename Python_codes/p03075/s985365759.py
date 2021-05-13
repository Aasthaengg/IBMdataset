import sys
import math
import bisect

def main():
    A = []
    for i in range(5):
        A.append(int(input()))
    m = int(input())
    ans = 'Yay!'
    for i in range(len(A)):
        for j in range(len(A)):
            if abs(A[i] - A[j]) > m:
                ans = ':('
    print(ans)
    
if __name__ == "__main__":
    main()
