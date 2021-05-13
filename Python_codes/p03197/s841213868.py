n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
for i in a:
    if i%2==1:
        print('first')
        break
else:
    print('second')