import sys
readline = sys.stdin.buffer.readline

def func(lst):
    res = 0
    for i in range(1,n):
        if lst[i]==lst[i-1]:
            res += 1
    return res


if __name__ == "__main__":
    n = int(readline())
    lst1 = list(map(int,readline().split()))
    lst1.sort()

    same = func(lst1)

    if same%2 != 0:
        print(n-same-1)
    else:
        print(n-same)
