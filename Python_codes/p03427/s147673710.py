n = int(input())
str_n = str(n)
n_1 = str_n[0]
tmp = int(n_1+"9"*(len(str_n)-1))
ans = int(n_1) + 9*(len(str_n)-1)

if n == tmp:
    print(ans)
else:
    print(ans-1)
