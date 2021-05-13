s = list(input())
k = int(input())

l = []
for i in range(len(s)):
    for y in range(k):
#        print(''.join(s[i:i+y+1]))
        if not ''.join(s[i:i+y+1]) in l:
            l.append(''.join(s[i:i+y+1]))

l.sort()
if not l:
    print(s[0])
else:
    print(l[k-1])
