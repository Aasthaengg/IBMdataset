N = int(input())
p = list(map(int,input().split()))
cnt = 0
flag = True
for i in range(N):
    if p[i] == i+1:
        if flag:
            cnt += 1
            flag = False
        else:
            flag = True
    else:
        flag = True
print(cnt)
    
