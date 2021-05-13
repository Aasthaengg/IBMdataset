k=int(input())
a,b=map(int, input().split())

if a % k == 0:
    print('OK')
elif int(b/k) - int(a/k) > 0:
    print('OK')
else:
    print('NG')