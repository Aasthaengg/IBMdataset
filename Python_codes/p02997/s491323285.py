from itertools import combinations
n,k = map(int,input().split())
if k > (n-1)*(n-2)//2:
    print(-1)
else:
    count = n-1 + (n-1)*(n-2)//2 - k
    ans = [(1,i) for i in range(2,n+1)]
    plus = (n-1)*(n-2)//2 - k
    print(count)
    num = 0
    rem = [i for i in range(2,n+1)]
    for a,b in combinations(rem,2):
        if num == plus:
            break
        ans.append((a,b))
        num += 1
    for a,b in ans:
        print(a,b)