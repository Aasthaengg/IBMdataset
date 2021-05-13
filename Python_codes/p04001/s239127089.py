s = input()
num = len(s)-1
ans = 0

if num == 0:
    print(int(s))
else:
    for i in range(2**num):
        mode = ['-']*num
        for j in range(num):
            if (i>>j)&1:
                mode[j] = '+'
        val = s[0]
        for k in range(num):
            if mode[k] == '+':
                if val != '':
                    ans += int(val)
                val = s[k+1]
            else:
                val += s[k+1]
            if val != '' and k == num-1:
                ans += int(val)
    print(ans)
    
