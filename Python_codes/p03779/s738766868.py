x = int(input())

for i in range(10**5):
    if 2*x <= (i+1)*i:
        print(i)
        break