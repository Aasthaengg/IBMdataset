n, k = map(int, input().split())
s = input()

state = '1'
cnt = 0
start = 0
ret = 0

for i in range(len(s)):
    if state == '1' and s[i] == '0':
        cnt += 1
        if cnt <= k:
            length = i - start + 1
            ret = max(ret, length)
        else:
            has_zero = False
            while True:
                if has_zero and s[start] == '1':
                    break
                else:
                    if s[start] == '0':
                        has_zero = True
                    start += 1
            length = i - start + 1
            ret = max(ret, length)
        state = '0'
    elif state == '1' and s[i] == '1':
        length = i - start + 1
        ret = max(ret, length)
    elif state == '0' and s[i] == '0':
        length = i - start + 1
        ret = max(ret, length)
    else:
        state = '1'
        length = i - start + 1
        ret = max(ret, length)

print(ret)

