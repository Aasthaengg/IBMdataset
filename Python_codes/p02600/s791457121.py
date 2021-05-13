X = int(input())
b = 400
cnt = 8
 
a = (X - b) // 200
for i in range(1,9):
    a = (X - b) // 200
    if  0 <= a < 1:
        print(cnt)
        break
    else:
        cnt -= 1
        b += 200