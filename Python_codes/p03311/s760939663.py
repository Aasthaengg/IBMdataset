def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    a1 = []
    for i in range(len(a)):
        a1.append(a[i]-i-1)
    a2 = sorted(a1)
    if len(a2)%2 == 0:
        mda = a2[len(a2)//2]
    else:
        mda = a2[(len(a2)-1)//2]
    ans = 0
    for i in range(len(a2)):
        ans += abs(mda-a2[i])
    print(ans)
resolve()