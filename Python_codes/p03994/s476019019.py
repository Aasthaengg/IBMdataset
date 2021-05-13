s = list(input())
k = int(input())
ls = list("abcdefghijklmnopqrstuvwxyz")
ls.sort(reverse=True)
ls = ["a"] + ls[:-1]
for i in range(len(s)):
    if i != len(s)-1:
        if k >= ls.index(s[i]):
            k -= ls.index(s[i])
            s[i] = "a"
        else:
            continue
    else:
        k %= 26
        s[-1] = ls[(ls.index(s[-1])-k)%26]
print("".join(s))