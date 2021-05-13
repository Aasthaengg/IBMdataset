from collections import defaultdict,deque
import math
def main():
    n = int(input())
    A=[int(i) for i in input().split()]
    dd = defaultdict(int)
    for i in A:
        dd[i]+=1
    lis = []
    for v in dd.keys():
        if(dd[v]>=4):
            lis.append(v)
            lis.append(v)
        elif(dd[v]>=2):
            lis.append(v)

    lis.sort(reverse = True)
    if(len(lis)<2):
        print(0)
    else:
        print(lis[0]*lis[1])



if __name__ == '__main__':
    main()
