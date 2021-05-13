a, b = map(int, input().split())
print('{0}'.format(a+b) if b%a==0 else '{0}'.format(b-a))