#https://atcoder.jp/contests/abc174/tasks/abc174_c
K= int(input())

if K%2==0 or K%5==0:
    print(-1)
elif K==1 or K==7:
    print(1)
else:
    B = 7
    i = 1
    while 1:
        if B==0:
            print(i)
            break
        else:
            B = (10 * B + 7) % K
            i = i + 1