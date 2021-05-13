n = int(input())
a = 0
for i in range(1,10):
    if n % i != 0:
        continue
    else:
        if n / i <= 9:
            a += 1
            break
        else:
            continue
if a == 1:
	print('Yes')
else:
	print('No')