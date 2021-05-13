H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
answer = [[0] * W] * H
# True_answer = []
input_list = []
for i in range(1, N+1):
    for _ in range(a[i-1]):
        input_list.append(i)

for i in range(H):
    for j in range(W):
        if i % 2 == 0:
            # print('2')
            answer[i][j] = input_list[W * i + j]
            # print(answer[0], answer[1], answer[2])
        else:
            # print('not2')
            answer[i][W-j-1] = input_list[W * i + j]
            # print(answer)
        if (j+1) % W == 0:
            # True_answer[i] += answer[i]
            print(*answer[i])



# print(input_list)
# print(answer)
# print(True_answer)
