r, g, b = list(map(int,input().split()))
try_cnt = int(input())

while r >= g:
    try_cnt -= 1
    g *= 2        
    
while g >= b:
    try_cnt -= 1
    b *= 2

if try_cnt >= 0:
    print('Yes')
else:
    print('No')   