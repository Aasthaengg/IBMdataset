s = int(input())

check = [0]*(10**6+1)
check[s]=1
counter = 1
while 1:
    counter +=1
    s = s//2 if s%2 ==0 else 3*s+1
    if check[s]==1:
        print(counter)
        break
    check[s]=1
