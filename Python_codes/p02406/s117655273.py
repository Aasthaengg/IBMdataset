n = int(input())
for i in range(1,n+1):
   x = i
   if x % 3 == 0:
        print('', i, end='')
   else:
        while True:
            if x % 10 == 3:
                print('', i, end='')
                break
            x //= 10
            if x == 0:
                break
print()