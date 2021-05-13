N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
A.sort(key=lambda x: x[2], reverse=True)
for c_x in range(101):
    for c_y in range(101):
        H = -1
        H_upper = 10**9
        for i, v in enumerate(A):
            if v[2] == 0:
                H_upper = min(H_upper, abs(c_x - v[0]) + abs(c_y - v[1]))
                if H_upper < H:
                    break
            else:
                tmp_H = abs(c_x - v[0]) + abs(c_y - v[1]) + v[2]
                if H == -1:
                    H = tmp_H
                elif H != tmp_H:
                    break
            if i == N-1:
                if H == -1:
                    print(c_x, c_y, H_upper)
                else:
                    print(c_x, c_y, H)
