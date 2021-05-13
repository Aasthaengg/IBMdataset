h = int(input())
c = 0
while True :
    h = h // 2
    c += 1
    if h == 0 :
        break
print(2**c-1)
