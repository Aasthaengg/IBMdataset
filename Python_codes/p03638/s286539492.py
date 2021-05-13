H, W = map(int, input().split())
N = int(input())
A = [int(x) for x in input().split()]
ans = [0] * H
for i in range(H):
    ans[i] = [0] * W
h_index = 0
A_index = 0
w_index = 0
now_num = 0
while (h_index != H):
    #print(h_index, w_index)
    ans[h_index][w_index] = A_index + 1
    now_num += 1
    if A[A_index] == now_num:
        now_num = 0
        A_index += 1
    if h_index % 2 == 0:
        if w_index == W-1:
            h_index += 1
        else:
            w_index += 1
    else:
        if w_index == 0:
            h_index += 1
        else:
            w_index -= 1
for j in range(H):
    print(*ans[j], sep=" ")
