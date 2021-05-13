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
    ret=0
    k,s = map(int,input().split())
    for x in range(k+1):
        for y in range(k+1):
            if 0 <= s-x-y <= k:
                ret+=1
    print(ret)
 
if __name__=='__main__':
    main()