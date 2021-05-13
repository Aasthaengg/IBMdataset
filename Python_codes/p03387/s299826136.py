def resolve():
    a, b, c = map(int, input().split())

    ans= 0
    even = []
    odd = []
    for i in [a, b, c]:
        if i % 2== 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        ans += 1 #奇数に+1
        odd[0] += 1
        odd[1] += 1
        m = max(max(even), odd[0]+1)
        even.extend(odd)
        for i in even:
            ans += (m-i)//2
    elif len(even) == 2:
        ans += 1 #偶数に+１
        even[0] += 1
        even[1] += 1
        m = max(max(even),odd[0])
        even.extend(odd)
        for i in even:
            ans += (m-i)//2
    elif len(even) == 3 or len(odd) == 3:
        m = max(max(even, odd))
        for i in max(even, odd):
            ans += (m-i)//2
    print(ans)
resolve()