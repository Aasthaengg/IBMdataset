import itertools
n, k = map(int,input().split())
a = [i for i in range(2,n+1)]
a_comb = list(itertools.combinations(a,2))
if k > (n-1)*(n-2) // 2:
    print(-1)
else:
    ans = []
    for i in range(2, n+1):
        ans.append((1, i))
    for i in range((n-1)*(n-2)//2 - k):
        ans.append((a_comb[i][0], a_comb[i][1]))
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


