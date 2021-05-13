a,b,c = map(int, input().split())
K = int(input())

cnt = 0
while b <= a:
    cnt += 1
    b *= 2
while c <= b:
    cnt += 1
    c *= 2
if cnt <= K:
    print('Yes')
else:
    print('No')