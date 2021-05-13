#D問題
N = int(input())

flag = 0
for i in range(2*N):
    I = i+1
    if I*(I+1) == 2*N:
        k = I+1
        flag = 1
        break
        
if flag == 0:
    print("No")
else:
    print("Yes")
    print(k)
    ans = [[] for i in range(k)]
    now = 0
    for i in range(k-1):
        loop = 1+i
        for j in range(loop):
            now+=1
            if j == 0:
                ans[0].append(now)
            if j == loop-1:
                ans[-1].append(now)
            if j > 0 and j < loop-1:
                ans[j].append(now)
            if i != 0:
                ans[i].append(now)
            
    for a in ans:
        print(len(a),end=" ")
        print(*a)