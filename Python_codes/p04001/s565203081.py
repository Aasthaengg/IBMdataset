s = input()
n = len(s)-1

total = 0
#digit loop
for b in range(2**n):
    nums = []
    index = 0
    #bit loop / looking for plus location until number of digit
    for i in range(n):
        if ( b & (1 << i) ):
            nums.append(int(s[index:i+1]))
            index = i+1
    nums.append(int(s[index:]))
    total = total + sum(nums)
print(total)