import heapq
from sys import stdin
input = stdin.readline

#入力
s = input()[0:-1]
# n = int(input())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]


# ab=[]
# for i in range():
#     a,b = map(int, input().split())
#     ab.append([a,b])


     
def main():
    if len(s)==2:
        print(s)
    else:
        print(s[::-1])
    
if __name__ == '__main__':
    main()