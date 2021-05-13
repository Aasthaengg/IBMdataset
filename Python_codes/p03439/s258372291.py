import sys
N = int(input())


def query(num):
    print(num)
    return input()


result = [-1] * (N + 1)
result[0] = query(0)
result[N] = result[0]
edge = [0, N]
if result[0] == "Vacant":
    sys.stdout.flush()
else:
    for i in range(30):
        idx = int(abs(edge[0] - edge[1]) / 2) + min(edge)
        result[idx] = query(idx)
        if result[idx] == "Vacant":
            sys.stdout.flush()
            break
        for i in range(2):
            r = result[edge[i]]
            if abs(edge[i] - idx) % 2 == 0:
                if r != result[idx]:
                    if i == 0:
                        edge[1] = idx
                        break
                    else:
                        edge[0] = idx
                        break
            elif abs(edge[i] - idx) % 2 == 1:
                if r == result[idx]:
                    if i == 0:
                        edge[1] = idx
                        break
                    else:
                        edge[0] = idx
                        break
    sys.stdout.flush()
