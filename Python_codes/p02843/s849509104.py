import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()[0:-1]
x = int(input())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


# ab=[]
# for i in range():
#     a,b = map(int, input().split())
#     ab.append([a,b])


     
def main():
   if x >2000:
       print(1)
   else:
        flag = False
        for i in range(21):
            for j in range(20):
                for k in range(20):
                    for l in range(20):
                        for m in range(20):
                            for n in range(20):
                                if 100*i + 101*j+ 102*k + 103*l + 104*m + 105*n == x:
                                    flag = True
        if flag :
            print(1)
        else:
            print(0)

    

if __name__ == '__main__':
    main()