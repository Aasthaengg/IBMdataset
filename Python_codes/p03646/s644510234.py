K = int(input())
q, mod = divmod(K, 50)
print(50)
pas = 50 + q - mod
for i in range(q, q + 51):
    if i == pas:
        continue
    print(str(i) + ' ', end='')
print('')
