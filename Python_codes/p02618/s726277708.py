D = int(input())
C = [int(i) for i in input().split()]
scores = [[int(i) for i in input().split()] for j in range(D)]
ans = [0]*D
S = 0
last = [0]*26
for d in range(1,D+1):
    m = -float("inf")
    index = -1
    for i,t in enumerate(scores[d-1]):
        st = S + t
        lt = [i for i in last]
        lt[i] = d
        for j in range(26):
            st -= C[j] * (d - lt[j])
        if m < st:
            m = st
            index = i
    S = m
    ans[d-1] = index+1
    last[index] = d
print("\n".join(map(str, ans)))