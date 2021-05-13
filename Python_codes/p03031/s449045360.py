n, m = map(int, input().split())
switch = [list(map(lambda x:int(x)-1, input().split()))[1:] for _ in range(m)]
rest = list(map(int, input().split()))
ans = 0
for bit in range(1<<n):
    for j in range(m):
        on_sum = 0
        for i in range(n):
            if bit >> i & 1 and i in switch[j]:
                on_sum += 1
        if on_sum % 2 != rest[j]:
            break
    else :
        ans += 1
print(ans)

