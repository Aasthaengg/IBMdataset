s = input()
ans = 0

a_stack = 0
i = 0
while i < len(s):
    v = s[i]
    if v == 'A':
        a_stack += 1
        pass
    elif v == 'B' and i < len(s)-1 and s[i+1] == 'C':
        ans += a_stack
        i += 1
    else:
        a_stack = 0
    i+=1
print(ans)
