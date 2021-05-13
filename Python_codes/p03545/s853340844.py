nums = list(map(int, list(input())))
ans = ''
for n in range(8):
    bits = bin(n)[2:].zfill(3)
    total = nums[0]
    ans = str(nums[0])
    for i, b in enumerate(bits):
        if b == '0':
            total += nums[i+1]
            ans += '+' + str(nums[i+1])
        else:
            total -= nums[i+1]
            ans += '-' + str(nums[i+1])

    if total == 7:
        ans += '=7'
        break

print(ans)