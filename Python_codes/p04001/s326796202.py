s = input()
#word = []
#for i in range(len(s)):
#    word.append(int(s[i]))
interval = len(s) - 1
ans = 0
for i in range(2**interval):
    f = list(s)
    for j in range(interval):
        if (i & (1<<j)):
            f[j] = f[j] + '+'
    f = "".join(f)
    #print(f)
    if '+' in f:
        #print(f.split('+'))
        ans = ans + sum(list(map(int,f.split('+'))))
    else:
        ans = ans + int(f)
print(ans)