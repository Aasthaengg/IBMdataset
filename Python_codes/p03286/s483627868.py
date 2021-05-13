N=int(input())
if N==0:
    print(0)
    exit()
ans = ""
tmp = N
while tmp != 0:
    div, mod = divmod(tmp, -2)
    if mod == -1:
        div += 1
        mod = 1
    ans += str(mod)
    tmp = div

print(ans[::-1])
