N = int(input())
alist = list(map(int, input().split()))
flag = 0
for i in range(0,N):
    if alist[i]%2 == 1:
        continue
    else:
        if alist[i]%3 == 0 or alist[i]%5 == 0:
            continue
        else:
            print("DENIED")
            flag = 1
            break
if flag == 0:
    print("APPROVED")