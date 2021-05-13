n = int(input())
s = [int(input()) for i in range(n)]
list.sort(s , reverse = True)
t = sum(s)

if t % 10 != 0:
    print(t)
else:
    i = -1
    j = True
    while j:
        if s[i] % 10 == 0:
            i -= 1
            if abs(i) > n:
                print(0)
                j = False
        else:
            print(t - s[i])
            j = False