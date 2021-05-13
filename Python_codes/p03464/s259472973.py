k = int(input())
arr = list(map(int,input().split()))
arr.reverse()

lower = 2
upper = 2
flag = True
for i in range(k):
    lowm = lower//arr[i]
    upm = upper//arr[i]

    if upm == 0:
        flag = False
    if arr[i] * lowm < lower:
        lowm += 1
        if lowm > upm:
            flag = False
    lower = arr[i] * lowm
    upper = arr[i] * upm + arr[i]-1
    # print(lowm,upm)
    # print(lower,upper)
    # print("##########")



if flag:
    print(lower,upper)
else:
    print(-1)
