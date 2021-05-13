import bisect

A,B,Q = map(int,input().split())

shira = [-100000000000] + [int(input()) for _ in range(A)] + [10000000000000]
temp = [-100000000000] + [int(input()) for _ in range(B)] + [10000000000000]

shira.sort()
temp.sort()

for _ in range(Q):
    x = int(input())
    shira_s = bisect.bisect_left(shira,x)
    temp_s = bisect.bisect_left(temp,x)
    ans = 100000000000
    for i in [shira_s-1,shira_s]:
        for j in [temp_s-1,temp_s]:
            ans = min(ans, abs(shira[i]-x)+abs(shira[i]-temp[j]))
            ans = min(ans, abs(temp[j]-x)+abs(temp[j]-shira[i]))
    print(ans)