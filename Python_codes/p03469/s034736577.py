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
    s = inputStrOnebyOne()
    s[3] = 8
    print(''.join(map(str,(s))))

if __name__=='__main__':
    main()