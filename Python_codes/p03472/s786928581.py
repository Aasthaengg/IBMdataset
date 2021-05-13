from collections import defaultdict,deque
import math
def main():
    n,h=map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    tmp = max([int(i[0]) for i in ab])
    bs = [int(i[1]) for i in ab]+[0]
    bs.sort(reverse = True)
    i = 0
    res = 0
    for i in bs:
        if i>=tmp:
            res+=1
            h-=i
            if(h<=0):
                break
        else:
            res += math.ceil(h/tmp)
            break

    print(res)





if __name__ == '__main__':
    main()
