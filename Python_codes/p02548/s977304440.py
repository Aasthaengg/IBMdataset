n = int(input())
cnt = 0
for a in range(1, n):
    bn = (n-1) // a
    for b in range(1, bn+1):
        c = n-(a*b)
        if c<=0: break
        if a*b + c == n:
            cnt += 1
print(cnt)
