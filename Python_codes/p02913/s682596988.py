n = int(input())
s = input()
left = 0
right = n // 2 + 1
while right - left > 1:
    mid = (right + left) // 2
    length = mid
    check = set()
    for i in range(n - length + 1):
        s1 = s[i:i+length]
        check.add(s1)
        if s[i+length: i + 2*length] in check:
            left = mid
            break
    else:
        right = mid
print(left)