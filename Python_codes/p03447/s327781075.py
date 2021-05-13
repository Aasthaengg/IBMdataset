X,A,B = [int(input()) for i in range(3)]

count = ((X-A)//B)
price = (X - A) - B*count
print(price)
