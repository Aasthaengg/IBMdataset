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
    x = int(input())
    a = int(input())
    b = int(input())
    x = x-a
    while b <= x:
        x-=b
    print(x)
    
if __name__=='__main__':
    main()