n = int(input())
s1 = input()
s2 = input()
mod = 10**9 + 7

if n == 1:
    print(3)
    exit()

yoko_flag = False
domino = []
for i in range(n-1):
    if s1[i+1] == s1[i]:  # yoko
        yoko_flag = True
        domino.append("yoko")
    elif s1[i+1] != s1[i] and yoko_flag:
        yoko_flag = False
    elif s1[i+1] != s1[i] and not yoko_flag:  # tate
        domino.append("tate")
    if i == n-2:
        if s1[i+1] != s1[i]:
            domino.append("tate")
#print(domino)
len_domino = len(domino)
pre_domino = domino[0]
if domino[0] == "yoko":
    ans = 6
else:
    ans = 3
for i in range(1, len_domino):
    if domino[i] == "tate" and pre_domino == "tate":
        ans = ans*2 % mod
        pre_domino = domino[i]
    elif domino[i] == "tate" and pre_domino == "yoko":
        ans = ans*1 % mod
        pre_domino = domino[i]
    elif domino[i] == "yoko" and pre_domino == "tate":
        ans = ans*2 % mod
        pre_domino = domino[i]
    elif domino[i] == "yoko" and pre_domino == "yoko":
        ans = ans*3 % mod
        pre_domino = domino[i]
print(ans)



