from collections import defaultdict
s = input()
n = len(s)
ans = -1

if len(s) < 26:
    alphabet_ls = [chr(i) for i in range(97, 97+26)]
    alphabet_dict = defaultdict(int)
    for i in range(n):
        alphabet_dict[s[i]] = 1
    for alphabet in alphabet_ls:
        if alphabet_dict[alphabet] == 0:
            ans = s + alphabet
            break

else:
    stock_ls = []
    for i in range(25,-1,-1):
        now = s[i]
        greater = []
        for stock in stock_ls:
            if now < stock:
                greater.append(stock)
        if greater:
            replacer = min(greater)
            ans = s[:i] + replacer
            break
        else:
            stock_ls.append(s[i])
print(ans)


