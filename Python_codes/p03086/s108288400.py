li = list(input())
ans = 0
num = 0
for i in range(len(li)):
    if li[i] == 'A' or li[i] == 'G' or li[i] == 'C' or li[i] == 'T':
        num += 1
    else:
        if ans < num:
            ans = num
        num = 0
if ans == 0:
    ans = num
if ans < num:
    ans = num
print(ans)