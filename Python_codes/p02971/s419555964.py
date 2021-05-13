n = int(input())
a_list = [int(input()) for _ in range(n)]
cp_list = a_list.copy()
cp_list.sort()
second_ans = cp_list[-2]
ans = cp_list[-1]
for i in range(n):
    if a_list[i] == ans:
        print(second_ans)
    else:
        print(ans)