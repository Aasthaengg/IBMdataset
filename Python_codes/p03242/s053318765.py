N = int(input())
l = []
for s in str(N):
    if s == '1':
        l.append('9')
    elif s == '9':
        l.append('1')
    else:
        l.sppend(s)
print(''.join(l))