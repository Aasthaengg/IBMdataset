# coding: utf-8
# Here your code !

def func():
    try:
        (n,m) = tuple( [ int(num) for num in input().rstrip().split(" ") ] )
        matrix = [ [int(num) for num in input().rstrip().split(" ")] for i in range(n) ]
        vector = [ int( input().rstrip() ) for i in range(m) ]
    except:
        return inputError()

    result = [ sum( [ matrix[j][i]*vector[i] for i in range(m) ] ) for j in range(n)  ] #????????¨??????????????????

    for num in result:
        print(num)
    
def inputError():
    print("input error")
    return -1

func()