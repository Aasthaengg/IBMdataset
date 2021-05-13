# E - Handshake

N, M = map(int, input().split())
A = list(int(x) for x in input().split())

A.sort(reverse=True)

S = []
S.append(A[0])
for i in range(N-1):
    S.append(S[i]+A[i+1])
S.append(0)

# 幸福度がX以上となる握手がM以上になることを考える
# つまり、幸福度がXより大きい(X+1以上)の握手と
# 幸福度がXの握手を足すとM以上

def CheckHappy(x):
    X = list(map(lambda y: x - y, A))
    cnt = 0
    happy = 0
    for i in range(N):
        l = -1
        r = N
        while l+1 < r:
            m = (l+r)//2
            if A[m] >= X[i]:
                l = m
            else:
                r = m 
        cnt += l+1
        if l>=0:
            #print(A[i], S[l])
            happy += A[i]*(l+1)+S[l]
    #print('cnt, happy', cnt, happy)
    return cnt, happy

def isGreaterThanM(x):
    X = list(map(lambda y: x - y, A))
    #print('X',X)
    cnt = 0
    for i in range(N):
        l = -1
        r = N
        #print('l, r', l, r)
        while l+1 < r:
            m = (l+r)//2
            if A[m] >= X[i]:
                l = m
            else:
                r = m 
        cnt += l+1
        #print('cnt',cnt)
        if cnt >= M:
            return True
    return False


# 2分探索
left = min(A)*2-1
right = max(A)*2+1

while left+1 < right:
    mid = (left+right)//2
    if isGreaterThanM(mid):
        left = mid
    else:
        right = mid

#print('left, right', left, right)

tmp, ans = CheckHappy(right)
ans += (M-tmp)*left
print(ans)


