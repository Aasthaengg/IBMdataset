def resolve():
    a, b = list(map(int, input().split(" ")))
    diff = b - a
    b_height = 0
    for i in range(1, diff+1):
        b_height += i
    print(b_height - b)    

if '__main__' == __name__:
    resolve()