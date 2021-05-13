s = input()
n = len(s) + 1
s = '<' + s + '>'

unfixed = set()
a = [0 for i in range(n+2)]
a[0] = -1
a[-1] = -1

for i in range(n+2):
    if i == 0 or i == n + 1 or s[i-1:i+1] == '><':
        j = i-1
        while 1 <= j <= n:
            if s[j-1:j+1] == '>>':
                a[j] = a[j+1] + 1
                j -= 1
            else:
                unfixed.add(j)
                break
        j = i + 1
        while 1 <= j <= n:
            if s[j-1:j+1] == '<<':
                a[j] = a[j-1] + 1
                j += 1
            else:
                unfixed.add(j)
                break

for j in unfixed:
    a[j] = max(a[j-1], a[j+1]) + 1

print(sum(a[1:-1]))