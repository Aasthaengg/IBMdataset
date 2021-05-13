n = int(input())
s = input()
num_red = 0
for c in s:
    if c == 'R':
        num_red = num_red + 1
if num_red > (n - num_red):
    print('Yes')
else:
    print('No')
