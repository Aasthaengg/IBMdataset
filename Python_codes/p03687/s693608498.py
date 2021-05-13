from copy import deepcopy
s = list(input())    
N = len(s)
count= 0
counter = []
ans = []
real = deepcopy(s)
syurui = set(s)
for j in syurui:
    while True:
        #終了条件
        if N == s.count(j):
            counter.append(count)
            count = 0
            s = deepcopy(real)
            N = len(s)
            break

        for i in range(N-1):
            if s[i]==j or s[i+1]==j:
                ans.append(j)
            else:
                ans.append(s[i])
        #値の更新
        N = len(ans)
        s = deepcopy(ans)
        count += 1

        #変数のリセット
        ans = []
print(min(counter))
