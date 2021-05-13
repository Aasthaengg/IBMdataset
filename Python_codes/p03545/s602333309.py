abcd = input()
n = len(abcd)
for i in range(1<<n-1):
    ans = abcd[0]
    for j in range(n-1):
        if i>>j&1:
            ans += "-" + abcd[j+1]
        else:
            ans += "+" + abcd[j+1]
    if eval(ans) == 7:
        print(ans+"=7")
        break