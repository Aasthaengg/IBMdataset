x = int(input())

ans = 100
cnt = 0
while ans < x:
    cnt+=1
    ans *= 101
    ans //= 100
print(cnt)