import sys, os

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    s = input()
    slen = len(s)
    cnt = [0] * 4
    mod = 1000*1000*1000+7
    cnt[0] = 1
    for i in range(slen):
        if s[i] == 'A':
            cnt[1] += cnt[0]
        elif s[i] == 'B':
            cnt[2] += cnt[1]
        elif s[i] == 'C':
            cnt[3] += cnt[2]
        else:
            cnt[0], cnt[1], cnt[2], cnt[3] =  3*cnt[0], 3*cnt[1] + cnt[0] , 3*cnt[2] + cnt[1], 3*cnt[3] + cnt[2]


        cnt[0]%= mod
        cnt[1]%= mod
        cnt[2]%= mod
        cnt[3]%= mod
    
    print(cnt[3])

solve()
