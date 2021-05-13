from collections import deque

if __name__ == "__main__":
    n, q = input().split()
    n, q = int(n), int(q)
    s = 0
    a = deque([list(map(str,input().split())) for _ in range(n)])

    while len(a):
        x = a.popleft()
        if int(x[1]) - q <= 0:
            s += int(x[1])
            print(x[0], s)
        else:
            x[1] = str(int(x[1]) - q)
            s += q
            a.append(x)
