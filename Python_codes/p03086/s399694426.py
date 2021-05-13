s = input()
ans = 0
tmp = 0
acgt = ['A','C','G','T']

for i in range(len(s)):
    if s[i] in acgt:
        tmp += 1
        if tmp > ans:
            ans = tmp
    elif tmp >= ans:
        ans = tmp
        tmp = 0

print(ans)
