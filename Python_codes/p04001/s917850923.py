S = input()
N = len(S) - 1

def add(n, s):
    if n == 0:
        tmp = 0
        for i in s.split('+'):
            tmp += int(i)
        return tmp
    else:
        st = s[:n] + '+' + s[n:]
        return add(n-1, st) + add(n-1, s)

print(add(N, S))