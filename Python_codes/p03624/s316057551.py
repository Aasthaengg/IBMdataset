s = input()

dic = "abcdefghijklmnopqrstuvwxyz"
nf = sorted(set(dic) - set(s))
ans = nf[0] if len(nf) > 0 else "None"

print(ans)
