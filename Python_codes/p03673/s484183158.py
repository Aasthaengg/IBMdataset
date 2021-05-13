from collections import deque

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = deque([])
    for i, tmp in enumerate(a):
        if i%2 == 0:
            b.append(tmp)
        else:
            b.appendleft(tmp)
    if n%2 == 1:
        b.reverse()
    print(*b)

if __name__ == "__main__":
    main()
