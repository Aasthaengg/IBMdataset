p = input()
n = int(p)

answer = False

q = input().split()
for i in range(n):
    s = q[i]
    if s == 'Y':
        answer = True
        break

if answer:
    print('Four')
else:
    print('Three')