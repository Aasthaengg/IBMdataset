from collections import deque
def main():
    n=int(input())
    x=deque()
    r=False
    for i in map(int,input().split()):
        if r:
            x.appendleft(i)
        else:
            x.append(i)
        r = not r
    if r:
        x.reverse()
    print(*x)

if __name__ == "__main__":
    main()