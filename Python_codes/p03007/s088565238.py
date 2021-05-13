from collections import deque
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))

    plus = []; minus = []
    for a in A:
        if a >= 0:
            plus.append(a)
        if a < 0:
            minus.append(a)
        
    plus.sort()
    minus.sort()
    plus = deque(plus)
    minus = deque(minus)

    if N == 2:
        if A[0] >= A[1]:
            ans = A[0] - A[1]
            print(ans)
            print(A[0], A[1])
        else:
            ans = A[1] - A[0]
            print(ans)
            print(A[1], A[0])
        return

    anslist = []
    if len(plus) == 0:
        stmp = minus.popleft()
        ltmp = minus.pop()
        anslist.append((ltmp, stmp))
        ans = ltmp - stmp
        plus.append(ans)
        N -= 1
    elif len(minus) == 0:
        stmp = plus.popleft()
        ltmp = plus.pop()
        anslist.append((stmp, ltmp))
        ans = stmp - ltmp
        minus.append(ans)
        N -= 1
    else:
        pass

    for _ in range(N):
        if len(minus) > 1:
            ltmp = plus.pop()
            stmp = minus.pop()
            anslist.append((ltmp, stmp))
            plus.append(ltmp - stmp)
        elif len(plus) > 1:
            ltmp = plus.popleft()
            stmp = minus.popleft()
            anslist.append((stmp, ltmp))
            minus.append(stmp - ltmp)
        else:
            ltmp = plus.popleft()
            stmp = minus.popleft()
            anslist.append((ltmp, stmp))
            ans = ltmp - stmp
            break
    print(ans)
    for s in anslist:
        print(*s)

if __name__ == "__main__":
    main()
