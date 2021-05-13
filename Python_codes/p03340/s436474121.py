
N = int(input())
A = list(map(int,input().split()))
#%%
bi = [[0]*20 for _ in range(N)]

state = [False]*20

for i,a in enumerate(A):
    tmp = a
    idx = 0
    while tmp>0:
        bi[i][idx] = tmp%2
        tmp >>= 1
        idx += 1

ans = 0
left = 0
right = 1

def upt(state,b):
    for i in range(20):
        if b[i]:
            state[i] = True
    return state
    
def rmv(state,b):
    for i in range(20):
        if b[i]:
            state[i] = False
    return state

def judge(state,b):
    for i in range(20):
        if state[i] and b[i]:
            return False
    return True

state = upt(state,bi[0])
#%%
while right<N:
    if judge(state,bi[right]):
        state = upt(state,bi[right])
        right += 1
    else:
        ans += right-left
        state = rmv(state,bi[left])
        left += 1

L = right - left
ans += L*(L+1)//2

print(ans)