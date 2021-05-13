from collections import deque

def main():
    dq = deque()
    n = int(input())
    for _ in range(n):
        com = input().split()
        if com[0]=='insert':dq.appendleft(com[1])
        elif com[0]=='delete':
            try:dq.remove(com[1])
            except:pass
        elif com[0]=='deleteFirst':dq.popleft()
        else:dq.pop()
    print(' '.join(dq))



if __name__ == '__main__':
    main()


