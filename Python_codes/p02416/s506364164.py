while True:
    s = input()
    if s == "0":
        break
    nums = list(s)
    goukei = 0
    for i in range(len(nums)):
        goukei += int(nums[i])
    print(goukei)