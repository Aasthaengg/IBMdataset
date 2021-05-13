k,t = map(int,input().split())
a = list(map(int,input().split()))
M = max(a)
if M <= -(-k//2):
    print(0)
else:
    if k % 2 == 0:
        print((M-k//2)*2-1)
    else:
        print((M+1-k//2)*2)