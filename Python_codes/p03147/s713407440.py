N = int(input())
h = [int(i) for i in input().split()]
end_flag = False
counter = 0
f = [0 for i in range(N)]
while end_flag == False:
    loop_flag = False
    flag = False
    for i in range(N):
        if f[i] < h[i]:
            flag = True
            loop_flag = True
            f[i] += 1
        else:
            if flag == True:
                counter += 1
                flag = False
    if flag == True:
        counter += 1
    if loop_flag == False:
        end_flag = True
print(counter)
