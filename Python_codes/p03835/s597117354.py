#-*-coding:utf-8-*-

def main2():
    k,s = map(int,input().split())
    counter=0
    for x in range(k+1):
        for y in range(k+1):
            if 0<=s-x-y <=k:
                counter+=1
    print(counter)

if __name__=="__main__":
    main2()