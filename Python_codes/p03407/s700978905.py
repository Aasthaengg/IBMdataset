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
    yen = inputOnebyOne_Int()
    if(yen[2] <= yen[0]+yen[1]):
        print("Yes")
    else:
        print("No")

if __name__=='__main__':
    main()