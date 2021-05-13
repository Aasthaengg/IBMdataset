def resolve():
    s = input()
    dict = {}
    k = 0
    for i in s:
        if i in dict:
            dict[i].append(k)
        else:
            dict[i] =[k]
        k += 1

    ans = 10**3
    for i in dict:
        test = dict[i]
        ans1 = test[0]
        for j in range(1,len(test)):
            ans1 = max(ans1, test[j]-test[j-1]-1)
        ans1 = max(ans1, (len(s)-test[-1]-1))
        ans = min(ans1,ans)
    print(ans)
resolve()