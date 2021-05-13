s = [int(input())]
for i in range(1000001):
    if s[i] % 2 == 0:
        s.append(s[i]/2)
    else:
        s.append(3 * s[i] + 1)
    if s[i] in s[:i]:
        print(i+1)
        break