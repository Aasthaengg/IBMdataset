n =int(input())
b = False
for i in range(int(n//1.08-1), int(n//1.08+4),1):
    if n == int(i*1.08):
        b = True
        break

if b == True:
    print(i)
else:
    print(':(')