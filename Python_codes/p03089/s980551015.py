N = int(input())
B = list(map(int, input().split()))
V = []

while B:
    # print(f'{B=}')
    for idx in range(len(B) - 1, -1, -1):
        if B[idx] == idx + 1:
            v = B.pop(idx)
            V.append(v)
            break
    else:
        print(-1)
        exit()

for v in V[::-1]:
    print(v)
