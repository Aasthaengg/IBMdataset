n = input()
len_n = len(n)
ans = "ABC" + n
if len_n == 1:
    ans = "ABC00" + n
elif len_n == 2:
    ans = "ABC0" + n
print(ans)