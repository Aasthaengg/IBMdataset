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
    a, b, c, d = map(int,input().split())
    if a+b > c+d:
        print("Left")
    elif a+b < c+d:
       print("Right")
    else:
        print("Balanced")

if __name__=='__main__':
    main()