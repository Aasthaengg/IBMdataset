# 1
# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_a
if False:
    print('YES' if set(input().split())==set(list('1974')) else 'NO')

# 2
# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b
if True:
    S=input()
    ans='NO'
    K='keyence'
    for i in range(len(S)-1):
        for j in range(i,len(S)):
            if S[:i+1]+S[j:]==K: ans='YES'
    print(ans)

# 3
# https://atcoder.jp/contests/aising2019/tasks/aising2019_a
if False:
    N=int(input())
    H=int(input())
    W=int(input())
    print((N-H+1)*(N-W+1))

# 4
# https://atcoder.jp/contests/aising2019/tasks/aising2019_b
if False:
    N=int(input())
    A,B=map(int,input().split())
    P=[int(i) for i in input().split()]
    cnt=[0,0,0]
    for p in P:
        if p<=A: cnt[0]+=1
        elif A<p<=B: cnt[1]+=1
        else: cnt[2]+=1
    print(min(cnt)) 

# 5
# https://atcoder.jp/contests/caddi2018b/tasks/caddi2018b_a
if False: print(input().count('2'))