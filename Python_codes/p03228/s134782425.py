A,B,K= map(int,input().split())
x = A
y = B
cnt = 0
while cnt<K:
    if cnt%2==0:
        y += x//2
        x = x//2
    else:
        x += y//2
        y = y//2
    cnt += 1
print(x,y)