ans = ['ABC', 'ARC', 'AGC']
R = int(input())

if R < 1200:
    i = 0
elif R < 2800:
    i = 1
else:
    i = 2
print(ans[i])
