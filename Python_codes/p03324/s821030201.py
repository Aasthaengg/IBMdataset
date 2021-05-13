d, n = map(int, input().split())
a = 100 ** d
counter = 0
for i in range(1,111) :
    num = a * i
    if i % 100 != 0 :
        counter += 1
        if counter == n :
            print(num)
            break
 
