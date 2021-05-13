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
    n, k = map(int, input().split())
    print(k*(k-1)**(n-1))
 
if __name__=='__main__':
    main()