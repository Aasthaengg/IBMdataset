import math

def main2():
    n=int(input())
    l = []
    for i in range(5):
        s = int(input())
        l.append(s)
    print(math.ceil((n)/min(l))+4)
if __name__ == '__main__':
    main2()
