import sys
s = input()
dic = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(s),0,-1):
    for j in dic:
        if not j in s[:i]:
            if i == len(s):
                print(s[:i]+j)
                sys.exit()
            else:
                if dic.index(s[i]) < dic.index(j):
                    print(s[:i]+j)
                    sys.exit()
else:
    if s[0] != "z":
        print(dic[dic.index(s[0])+1])
    else:
        print(-1)