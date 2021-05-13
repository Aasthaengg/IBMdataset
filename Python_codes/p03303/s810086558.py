s = list(input())
w = int(input())
print(''.join([s[i] for i in list(range(0,len(s),w))]))
