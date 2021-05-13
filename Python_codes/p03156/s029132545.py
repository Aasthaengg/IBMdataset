# 1
# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_a
if False:
    print('YES' if set(input().split())==set(list('1974')) else 'NO')

# 2
# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b
if False:
    S=input()
    ans='NO'
    K='keyence'
    for i in range(len(K)):
        l=K[:i]
        r=K[i:]
        # print(l,r)
        if l in S and r in S:
            l_i=S.index(l)
            for j in range(len(S)):
                # print(S[j:j+len(K)-1])
                if j+len(r)-1<len(S) and S[j:j+len(r)]==r:
                    r_i=j
            # print(l_i,r_i)
            if l_i<=r_i:
                ans='YES'
                break
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
N=int(input())
A,B=map(int,input().split())
P=[int(i) for i in input().split()]
cnt=[0,0,0]
for p in P:
    if p<=A: cnt[0]+=1
    elif A<p<=B: cnt[1]+=1
    else: cnt[2]+=1
print(min(cnt)) 