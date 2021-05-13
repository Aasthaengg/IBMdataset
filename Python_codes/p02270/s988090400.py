def check(P):
    i = 0
    for j in range(k):
        s = 0
        while s + T[i] <= P:
            s += T[i]
            i += 1
            if i == n: return n
    return i

def solve():
    left, right = 0, 100000*10000
    while right - left > 1:
        mid = (left + right) / 2
        v = check(mid)
        if v >= n: right = mid
        else: left = mid
    return right

if __name__ == '__main__':
    T = []
    n, k = [int(x) for x in input().split()]
    for i in range(n): T.append(int(input()))    
    print(int(solve()))
