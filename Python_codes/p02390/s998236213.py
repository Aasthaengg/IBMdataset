num = int(input())
h = num // 3600
m = num % 3600 // 60
s = num % 3600 % 60
print('{}:{}:{}'.format(h, m, s))
