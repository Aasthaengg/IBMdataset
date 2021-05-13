n = int(input())
s = input()
t = input()

if (n == len(s) and (s == t)):
    print(n)
else:
    ind = [0]
    for i in range(1, len(s)):
        if s[-i:] == t[:i]:
            ind.append(i)

    ind.reverse()
    for i in ind:
        if i == 0:
            print(2*n)
        else:
            res = s[0:-i] + t
            if len(res) >= n:
                print(len(res))
                break