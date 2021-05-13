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
    a,b = input().split()
    if int(a)*int(b)%2==0:
        print("Even")
    else:
        print("Odd")

if __name__=='__main__':
    main()