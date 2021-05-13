n = int(input())
a_ls = list(map(int, input().split()))
a_ls = [0] + a_ls
box_ls = [0] * (n+1)
root = n ** 0.5
for i in range(n,0,-1):
    if 2*i > n:
        box_ls[i] = a_ls[i]
    else:
        Sum = 0
        num = i + i
        # ここの条件式不安あり
        while num <= n:
            Sum += box_ls[num]
            num += i
        rest = Sum % 2
        if (rest == 1 and a_ls[i] == 1) or (rest == 0 and a_ls[i] == 0):
            box_ls[i] = 0
        else:
            box_ls[i] = 1
ans_ls = []
for box_name, ball_num in enumerate(box_ls[1:],1):
    if ball_num == 1:
        ans_ls.append(str(box_name))
M = len(ans_ls)
print(M)
if M > 0:
    print(' '.join(ans_ls))

