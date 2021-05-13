N, M = list(map(int,input().rstrip().split()))
k = []
s = []
for i in range(M):
    stdin = list(map(int,input().rstrip().split()))
    k.append(stdin[0])
    s.append(stdin[1:])
p = list(map(int,input().rstrip().split()))
ans = 0
for bit in range(2**N):
    od = 0
    for j in range(M):
        odd = 0
        for sw in s[j]:
            mask = 1 << (sw-1)
            if bit&mask: # 右からi番目にビットが立っているかどうか判定
                odd += 1
        if p[j] != odd%2:
            break
    else:
        ans += 1
print(ans)