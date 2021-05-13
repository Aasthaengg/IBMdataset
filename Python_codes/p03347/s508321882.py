# AGC024C

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))


def main():
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = int(input())

    prev = a[-1]
    if a[0]!=0:
        print(-1)
        return
    count = 0
    for num in a[::-1]:
        if prev==num+1:
            pass
        elif prev >= num+2:
            print(-1)
            return
        else:
            count += num
        prev = num
    print(count)
main()