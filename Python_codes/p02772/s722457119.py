n = int(input())
a = list(map(int, input().split()))

for num in a:
    if num % 2 == 0:
        if num%3==0 or num%5==0:
            pass
        else:
            print('DENIED')
            exit()

print('APPROVED')