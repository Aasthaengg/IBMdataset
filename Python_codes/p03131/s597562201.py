import sys,math,collections,itertools
input = sys.stdin.readline
cnt =1
K,A,B=list(map(int,input().split()))
if A+2<=B:#交換したほうがいい
    if A-1 >=K:#最低交換枚数に達しない
      cnt = 1+K
    else:
        cnt = A + (K-(A-1))//2*(B-A)+(K-(A-1))%2
else:
    cnt = 1+K
print(cnt)

