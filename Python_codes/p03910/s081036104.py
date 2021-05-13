N = int(input())
ans = [0]
rui = 0
for i in range(1,N+1):
    ans.append(i)
    rui += i
    if rui >= N:
        break
for i in range(1,len(ans)):
    if i == (rui-N):
        continue
    print(ans[i])