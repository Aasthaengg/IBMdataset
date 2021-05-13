s = int(input())
ans = 0
a = list()
n = s
for i in range(100000) :
    if n in a :
        print(ans+1)
        break
    if n % 2 == 0 :
        a.append(n)
        n = n / 2
        ans += 1
    else :
        a.append(n)
        n = 3 * n + 1
        ans += 1
