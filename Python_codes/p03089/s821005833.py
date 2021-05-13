def solve(n, b):
    a = []
    while b:
        m = len(b)
        tj = -1
        for j in range(m, 0, -1):
            if b[j-1] == j:
                tj = j
                break
        if tj == -1:
            return -1
        else:
            a.append(tj)
            b = b[:tj-1] + b[tj:]
    return "\n".join(map(str, a[::-1]))

n = int(input())
b = list(map(int, input().split()))
print(solve(n, b))