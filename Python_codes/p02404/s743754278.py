def sh(num):
    for n in num:
        out(n)
def out(n):
    number = []
        # print(n[0])
        # print(n[1])
    for i in range(n[1]):
        number.append("#")
    for i in range(1,n[0]+1):
        if i in range(2,n[0]):
            print('#' + '.' * (n[1]-2) + '#')
        else:
            print(''.join(number))
    print('')

num = []
while True:
    n = list(map(int, input().split()))
    if n[0] == 0 and n[1] == 0:
        break
    else:
        num.append(n)
sh(num)