N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
answer_list = [0]*N

for i in range(N):
    temp = B_list[i]

    for j in range(i, i+2):
        if temp - A_list[j] <= 0:
            answer_list[i] += temp
            A_list[j] -= temp
            break
        else:
            answer_list[i] += A_list[j]
            temp -= A_list[j]
            A_list[j] -= A_list[j]

print(sum(answer_list))
