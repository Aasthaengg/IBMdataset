
N,K = map(int,input().split())
A = list(map(int,input().split()))

#%%
divisor = []
SA = sum(A)
for i in range(1,int(SA**0.5+1)):
    if i*i == SA:
        divisor.append(i)
    elif SA%i==0:
        divisor.append(i)
        divisor.append(SA//i)

divisor.sort()

def judge(x):
    # 全てのAiをK回以下の操作で0(mod x)にできるか？
    modlist = []
    for a in A:
        b = a%x
        modlist.append([b, x-b])
    modlist.sort()
    sum1 = [0]*(N+1)
    sum2 = [0]*(N+1)
    idx = 0
    for b,c in modlist:
        sum1[idx+1] = sum1[idx] + b
        sum2[idx+1] = sum2[idx] + c
        idx += 1
    
    res = 10**10
    for i in range(1,N+1):
        tmp = max(sum1[i], sum2[N]-sum2[i])
        res = min(res, tmp)
    
    if res>K:
        return False
    else:
        return True
    
ok = 1
for d in divisor:
    if judge(d):
        ok = d


print(ok)




