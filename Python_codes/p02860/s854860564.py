n = int(input())
s = input()
ct = 0
if n % 2:
    print("No")
    exit()
else:
    m = n//2
    for i in range(m):
        if s[i] != s[i+m]:
            ct +=1
if ct == 0:
    print('Yes')
else:
    print('No')
