x = int(input())

year = 1
b = 100
while True:
    b = b + b//100
    if b >= x:
        print(year)
        break
    else:
        year +=1
  
