x = int(input())
q,mod = divmod(x,11)
count=q*2
while True:
    if mod <= 0:
        print(count)
        break
    mod -= 6
    count += 1
    if mod <= 0:
        print(count)
        break
    mod -= 5
    count += 1
    
