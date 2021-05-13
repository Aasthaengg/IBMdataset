d, g = map(int, input().split())
A, B = [], []
for _ in range(d):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = float('inf')

for i in range(2**d):
    s, k = 0, 0 #s:得点, k:解いた問題数

    for j in range(d):
        if (i>>j)&1:
            s+=A[j]*(j+1)*100 + B[j] #pj+1問全て解く
            k+=A[j] #解いた問題数
    if s >= g:
        ans = min(ans, k)
    else:
        for l in range(d-1, -1, -1):
            if (i>>l)&1 == 0: #これまでにまだ解いていない問題
                if s+(l+1)*100*A[l]<g: #全部解いても超えない
                    s+=(l+1)*100*A[l]
                    k+=A[l]
                else:
                    rem = g-s #目標点までの残りの点数
                    k += -(-rem//(l+1)//100)
                    ans = min(ans, k)
print(ans)                
