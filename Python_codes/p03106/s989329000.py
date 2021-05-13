A,B,K = map(int,input().split())
ct = 0
for i in range(101,0,-1):
    if (A % i == 0) & (B % i == 0):
        ct += 1
        if ct == K:
            break

print(i)