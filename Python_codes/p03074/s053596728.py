n, k = map(int, input().split())
s = input()

counts = []
tmp = []
for i in range(len(s)):
    if tmp == []:
        tmp = [s[i], 1]
    else:
        if tmp[0] == s[i]:
            tmp[1] += 1
        else:
            counts.append(tmp)
            tmp = [s[i], 1]
if tmp:
    counts.append(tmp)

zero_ints = 0
for char, count in counts:
    if char == '0':
        zero_ints += 1

if counts[0][0] == '0':
    left = 0
else:
    left = 1
right = left - 2

used = 0
l = 0
for char, count in counts:
    if char == '0':
        if used < k:
            used += 1
            right += 2
        else:
            break
    l += count

ans = l
for i in range(zero_ints):
    l = l - counts[left][1]
    if left - 1 >= 0:
        l-= counts[left - 1][1]
    if right + 2 < len(counts):
        l += counts[right + 2][1]
    if right + 3 < len(counts):
        l += counts[right + 3][1]
    ans = max(ans, l)
    left += 2
    right += 2
    # print(left, right, l)
print(ans)
