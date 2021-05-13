n=int(input())
for i in range(1,10000):
    num=2**i-1
    if n<=num:
        print(num)
        break