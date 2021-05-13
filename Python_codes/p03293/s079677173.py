s,t = open(0).read().split()

if any(t == s[i:]+s[:i] for i in range(len(s))):
    print('Yes')
else:
    print('No')