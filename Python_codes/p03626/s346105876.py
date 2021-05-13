from collections import deque
def main():
    n = int(input())
    S1 = deque(list(input()))
    S2 = deque(list(input()))
    mod = 1000000007
    A = []
    while S1:
        s1 = S1.popleft()
        s2 = S2.popleft()
        if s1 == s2:
            A.append(0)
        else:
            S1.popleft()
            S2.popleft()
            A.append(1)
    if A[0] == 0:
        ans = 3
    else:
        ans = 6
    for i in range(1, len(A)):
        if A[i] == 0:
            if A[i - 1] == 0:
                ans = ans * 2 % mod
            else:
                pass
        else:
            if A[i - 1] == 0:
                ans = ans * 2 % mod
            else:
                ans = ans * 3 % mod
    print(ans)



if __name__ == '__main__':
    main()
