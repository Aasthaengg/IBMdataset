# We Love Golf

k = int(input())
a, b = map(int, input().split())

c = int(b/k) - int((a-1)/k)

if c==0:
    print('NG')
else:
    print('OK')