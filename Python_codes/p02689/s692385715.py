n,m = list(map(int,input().split()))
harr = list(map(int,input().split()))
ans = [True] * n
for i in range(m):
    a,b = list(map(int,input().split()))
    s = harr[a-1]; t = harr[b-1]
    if s > t:
        ans[b-1] = False
    elif s < t:
        ans[a-1] = False
    else:
        ans[a-1] = ans[b-1] = False

print(sum(ans))