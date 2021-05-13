a, b, k = map(int, input().split())
t = 100
cnt = 0
while t > 0:
    if a%t == 0 and b%t == 0:
        cnt+=1
        if cnt == k: break
    t-=1
print(t)