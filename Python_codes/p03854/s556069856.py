S = input()
S_r = S[::-1]

Ss = ["remaerd","resare","esare","maerd"]

ind = 0
while ind < len(S):
    flg = False
    for s in Ss:
        n = len(s)
        if S_r[ind:ind+n] == s:
            ind += n
            flg = True
    if not flg:
        print("NO")
        exit()
print("YES")