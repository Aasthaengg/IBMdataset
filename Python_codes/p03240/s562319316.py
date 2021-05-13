from sys import stdin
input = stdin.buffer.readline

def main():
    n = int(input())
    x = [-1] * n; y = [-1] * n; h = [-1] * n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())

    # full search
    for i in range(n):
        if h[i] > 0:
            ind = i
            break

    for cx in range(101):
        for cy in range(101):
            try:
                height = h[ind] + abs(x[ind] - cx) + abs(y[ind] - cy)
            except:
                # h == [0] * n
                height = 1

            flag = True
            for i in range(n):
                if h[i] == 0:
                    if height - abs(x[i] - cx) - abs(y[i] - cy) > 0:
                        flag = False
                        break
                else:
                    if height - abs(x[i] - cx) - abs(y[i] - cy) != h[i]:
                        flag = False
                        break
            if flag:
                print(cx, cy, height)
                exit()

main()