N = int(input())
a_list = [int(input())-1 for i in range(N)]
next_i = 0
done_flag = False
for i in range(N):
    next_i = a_list[next_i]
    if  next_i == 1:
        done_flag = True
        break

if done_flag:
    print(i + 1)
else:
    print(-1)