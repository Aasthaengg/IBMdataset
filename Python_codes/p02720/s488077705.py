from collections import deque
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    k=INT()
    que=deque([1,2,3,4,5,6,7,8,9])
    for i in range(k):
        q=que.popleft()
        if q%10!=0:
            que.append(10*q+q%10-1)
        que.append(10*q+q%10)
        if q%10!=9:
            que.append(10*q+q%10+1)
        
    print(q)
if __name__ == '__main__':
    do()