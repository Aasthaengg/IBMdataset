nums = list(map(str, input().split()))
flg = False
if len(set(nums)) != 4:
    pass
else:
    for num in nums:
        if num in "1974":
            flg = True
        else:
            flg = False
            break
if flg == True:
    print("YES")
else:
    print("NO")