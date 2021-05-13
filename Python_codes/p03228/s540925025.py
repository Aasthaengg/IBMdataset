A,B,K=map(int,input().split())
cnt=0
while True:
    if A % 2 == 1:
        A -= 1
    B += A // 2
    A //= 2
    cnt += 1
    if cnt >= K:
        break
    if B % 2 == 1:
        B -= 1
    A += B // 2
    B //= 2
    cnt += 1
    if cnt >= K:
        break
print('{} {}'.format(A,B))