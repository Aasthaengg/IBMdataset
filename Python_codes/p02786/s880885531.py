H = int(input())

layer = 1
atack_cnt = 1

while True:
    if H == 1:
        print(atack_cnt)
        exit()
    
    elif H > 1:
        H = int(H/2)
        atack_cnt += layer*2
        layer *= 2
    
