N = int(input())
result = False
for i in range(1, 10):
    if N % i == 0 and N // i < 10:
        result = True
        break
if result:
    print('Yes')
else:
    print('No')