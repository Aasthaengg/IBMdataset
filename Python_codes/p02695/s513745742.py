import itertools
n,m,q = list(map(int,input().split()))
abcd = [list(map(int,input().split())) for i in range(q)]

ans = 0
for iter in itertools.combinations_with_replacement(range(1,m+1),n):
    result = 0
    for i in range(q):
        a,b,c,d = abcd[i][0],abcd[i][1],abcd[i][2],abcd[i][3]
        if iter[b-1] - iter[a-1] == c:
            result += d
    ans = max(ans, result)

print(ans)
