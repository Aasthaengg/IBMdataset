s = input().rstrip()
n = len(s)

def value(m):
    num = s[0]
    ans = 0
    for i in range(1, n):
        t = (m>>(i-1)) & 1
        if t ==1:
            ans += int(num)
            num = s[i]
        else:
            num = num + s[i]
    ans += int(num)
    return ans

count = 0
for i in range(2**(n-1)):
    count +=value(i)

print(count)