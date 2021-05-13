A = list(map(int, input().split()))

def hantei(list):
    #a + b = X and 2a + 4b = Y が存在するか
    #条件1 1 <= a <= 100 and 1 <= b <= 100

    a = 0
    count = 0
    while a <=100:
        for b in range(101):
            if a + b == list[0] and 2 * a + 4 * b == list[1]:
                print("Yes")
                count = 1
                break
        a += 1
        if count == 1:
            break
        elif count == 0 and a >= 100:
            print("No")
            break 

hantei(A)

