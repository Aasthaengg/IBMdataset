s = input()
n = len(s)

for i in range(2, n, 2):
    left = int((n-i)/2)
    tmp1 = s[0:left]
    tmp2 = s[left:n-i]
    if (tmp1 == tmp2):
        print(left * 2)
        break