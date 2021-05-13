n = int(input())
a_l = list(map(int,input().split()))

num = 1
flag = -1 # -1:initial, 0:increasing, 1:decreasing
for i in range(1,n):
    if a_l[i] > a_l[i-1]:
        new_flag = 0
    elif a_l[i] < a_l[i-1]:
        new_flag = 1
    else:
        continue
    if new_flag != flag:
        if flag == -1:
            flag = new_flag
        else:
            flag = -1
            num += 1

print(max(num,1))

    

