import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()[0:-1]
# n = int(input())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


# ab=[]
# for i in range():
#     a,b = map(int, input().split())
#     ab.append([a,b])


     
def main():
    count =[0]*4
    for i in range(3):
       a,b = map(int, input().split())
       count[a-1]+=1
       count[b-1]+=1
    flag = True
    for i in count:
        if i ==3:
            flag=False
    if flag:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()