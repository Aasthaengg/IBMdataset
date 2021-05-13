from sys import exit
a,b,c = map(int,input().split())
cnt = 0
while ~a&1 and ~b&1 and ~c&1:
    newa = b//2+c//2
    newb = a//2+c//2
    newc = a//2+b//2
    a,b,c = newa,newb,newc
    cnt += 1
    if cnt >= 10**5:
        exit(print(-1))
print(cnt)