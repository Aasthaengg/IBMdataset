import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
cnt = 0
#-A1がマイナスならXと同じにならない-#
a1 = int(input())
if a1 != 0:
    print(-1)
#-A1<A2=A1+1なら+1,それ以外なら-1#
else:
    before = a1
    for i in range(1,N):
        a1 = int(input())
        if a1 == 0:
            continue
        elif a1==before+1:
            cnt += 1
        elif a1 <= before:
            cnt += a1
        else:
            print(-1)
            exit()
        before = a1
    print(cnt)
