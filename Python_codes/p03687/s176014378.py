s = input()
s_str = set(list(s))
ans = 101
for char in s_str:
    t = s
    count = 0
    while len(set(list(t))) > 1:
        next_t = ''        
        for i in range(len(t) - 1):
            if (t[i] == char) | (t[i + 1] == char):
                next_t += char
            else:
                next_t += t[i]
        t = next_t
        count += 1
    ans = min(ans, count)
print(ans)