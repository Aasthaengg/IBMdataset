from collections import deque

def main():
    n = input()
    A = deque(map(int,raw_input().split()))
    q = input()
    M = map(int,raw_input().split())

    p = rec([0],A)

    for m in M:
        if m in p:
            print "yes"
        else:
            print "no"

def rec(a,A):
    if len(A) == 0:
        return a
    else:
        y = A.popleft()
        a = a+[x+y for x in a]
        return rec(a,A)

if __name__ == "__main__":
    main()