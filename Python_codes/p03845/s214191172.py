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
    n = int(input())
    tlist = inputOnebyOne_Int()
    m = int(input())

    ret=0
    for i in range(m):
        p,x = map(int, input().split())
        ret = sum(tlist) - tlist[p-1] + x
        print(ret)
 
if __name__=='__main__':
    main()