import collections

#文字列を一文字ずつ取得したいとき
def inputStrOnebyOne():
    s = list(input())
    return s

#整数を一つずつリストに入れる
def inputOnebyOne_Int():
    a = list(int(x) for x in input().split())
    return a

def main():
    a = inputStrOnebyOne()
    b = inputStrOnebyOne()
    c = inputStrOnebyOne()
    print(a[0]+b[1]+c[2])

if __name__=='__main__':
    main()