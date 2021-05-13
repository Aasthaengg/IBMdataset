
def main(x):
    a = x[0]
    b = x[1]
    c = x[2]
    if a < b and b < c:
        print('Yes')
    else:
        print('No')
        
    
if '__main__' == __name__:
    try:
        while True:
            main(list(map(int, input().strip().split(' '))))
    except EOFError:
        pass

