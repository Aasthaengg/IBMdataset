n = int(input())
As = list(map(int, input().split()))

# ps = [0] * (n+1)
# qs = [0] * (n+1)
# ps[-1] = As[-1]
# qs[-1] = As[-1]

p = As[-1]
q = As[-1]
Asr = As[::-1]
qs = [q]
# 深い方から見ていく
for j,a in enumerate(Asr[1:]):
    i = n - (j + 1) 
    p = (p+1)//2 + a 
    q = min(q + a, 2**i)

    # 最小値が、2**iを超えると、深さ0畳めないのでアウト
    if p > 2**i:
        print(-1)
        exit()
    
    # 2**iを超えない範囲での最大値
    qs.append(q)    
    
if p != 1:
    print(-1)
    exit()
qs.reverse()

qs[0] = 1
ans = 1
for i in range(1,n+1):
    if qs[i] > 2**i:
        qs[i] = 2 ** i
    if qs[i] > 2*(qs[i-1]-As[i-1]):
        qs[i] = 2 * (qs[i-1]-As[i-1])
    ans += qs[i]
print(ans)