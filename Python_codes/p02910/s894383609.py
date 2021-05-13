s = input()
ans = 0
for i in range(1,len(s)+1):
    if i%2 == 1:
        if s[i-1] == "R" or s[i-1] == "U" or s[i-1] == "D":
            ans += 1
        else:
            print('No')
            exit()
    elif i%2 == 0:
        if s[i-1] == 'L' or s[i-1] == "U" or s[i-1] == "D":
            ans += 1
        else:
            print('No')
            exit()
if ans == len(s):
    print('Yes')
else:
    print('No')