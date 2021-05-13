s = input()
n = len(s)
cnt = 0
s1 = s[:((n-1)//2)]
s2 = s[(n+3)//2 -1:n]

for i in range(n//2):
    if s[i] != s[-i-1]:
        print('No')
        exit()
    else:
        if s1[i] != s2[i]:
            print('No')
            exit()
print('Yes')