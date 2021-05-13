chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]

arr = []

x = int(input())

while True:
    s = x % 26
    arr.append(s)

    t = (x - 1) // 26
    # print("s,t", s, t)
    if t == 0:
        break
    x = t

# print('arr', arr)

ans = ""
for t in arr:
    if t == 0:
        ans += 'z'
    else:
        ans += chars[t - 1]

ans = ans[::-1]
print(ans)
