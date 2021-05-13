a, op, b = input().split()  #=input().split() : a, op, b 入力時はスペースあり
                            #a, op, b　入力時はスペースなし

if op == '+':
    print(int(a)+int(b))
elif op == '-':
    print(int(a)-int(b))