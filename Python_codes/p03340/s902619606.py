n = int(input())
al = list(map(int,input().split()))

head = 0
tail = 0
sub = 0
ll = 0
ans = 0
while True:
    if sub + al[tail] == sub ^ al[tail]:
        ll += 1
        if tail == n-1:
            for i in range(ll+1):
                ans += i
            break
        sub += al[tail]
        tail += 1
    else:
        ans += ll
        ll -= 1
        sub -= al[head]
        head += 1

print(ans)