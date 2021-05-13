a, b, c = map(int, input().split())
a_tmp = a ; b_tmp = b ; c_tmp = c
count = 0
while True :
    if a == b == c and a%2 == 0 :
        print("-1")
        break
    elif a%2 == 1 or b%2 == 1 or c%2 == 1 :
        print(count)
        break
    else :
        a = b_tmp/2 + c_tmp/2
        b = a_tmp/2 + c_tmp/2
        c = a_tmp/2 + b_tmp/2
        a_tmp = a ; b_tmp = b ; c_tmp = c
        count += 1
