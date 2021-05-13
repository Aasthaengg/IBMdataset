def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    import numpy as np
    a = np.array(A[::-1], dtype=int)
    ans = 0
    for i, b in enumerate(B[::-1]):
        tmp = (b - (a[i] + ans)%b) % b
        ans += tmp
    print(ans)


        

if __name__ == '__main__':
    main()