#/usr/bin/python

def solve():
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)
    a2 = [0] * len(a) * 2
    for i in range(len(a2)):
        a2[i] = a[i//2]
        if i >= n:
            break
    a2[0] = 0
    return sum(a2[:n])

print(solve())
