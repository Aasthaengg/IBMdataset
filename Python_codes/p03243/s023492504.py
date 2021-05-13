n = int(input())

if n % 111 == 0:
    print(n)
    quit()

print((n//111+1)*111)