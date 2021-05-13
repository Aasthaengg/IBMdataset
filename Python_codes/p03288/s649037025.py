R = int(input())
res = ''
if R < 1200:
    res = 'ABC'
elif R < 2800:
    res = 'ARC'
else:
    res = 'AGC'
print(res)