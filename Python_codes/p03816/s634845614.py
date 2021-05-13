import math
import collections
def main():
    n = int(input())
    A=[int(i) for i in input().split()]
    dd = collections.defaultdict(int)

    for i in A:
        dd[i]+=1
    yama = []
    for i in dd.keys():
        yama.append([i,dd[i]])

    yama.sort(key = lambda x:x[0])
    yama_l = len(yama)
    cnt=0
    renozku = False
    for i in range(yama_l-1):
        if(yama[i][1]==2 and yama[i+1][1]==2):
            renzoku = True

        if(yama[i][1]%2==0):
            cnt+=1
    if(yama[-1][1]%2==0):
        cnt+=1
    if(cnt==2 and renzoku):
        print(len(yama)-1)
    elif(cnt%2==1):
        print(len(yama)-1)
    else:
        print(len(yama))
if __name__ == '__main__':
    main()
