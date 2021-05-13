S = int(input())
p=(10**9)+7

ans_=[0,0,0]

N = 2000
for s in range(3,N+1):
#     print('===',s)
    a = 1
    s = s-3
    while s >= 0:
        if s < 0:
            break
        a += ans_[s]
#         print(s,a)
        s-=1
    ans_.append(a)

print(ans_[S]%p)