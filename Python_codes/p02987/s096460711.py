s = input()
if len(set(s)) == 2 and sum(s[i] == s[-i] for i in range(4))%2 == 0:
    print('Yes')
else:
    print('No')