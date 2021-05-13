N, M = map(int, input().split())
ks = []
for _ in range(M):
    ks.append(list(map(int, input().split())))
p = list(map(int, input().split()))

ans = 0
for bit in range(2**N):
    on_list = []
    for i in range(N):
        if bit & (1 << i):
            on_list.append(i+1)
    flag = True
    for s, p_ in zip(ks, p):
        on_sum = len(list(set(on_list) & set(s[1:])))
        if on_sum % 2 != p_:
            flag = False
            break
    
    if flag:
        ans += 1
        
print(ans)