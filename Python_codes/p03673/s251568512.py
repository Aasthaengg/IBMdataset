from collections import deque
def solve():
    n = int(input())
    A = list(map(int,input().split()))

    q = deque()
    for i in range(n):
        if i % 2 == 0:
            q.append(A[i])
        else:
            q.appendleft(A[i])
    
    ans = list(q)
    if n % 2 != 0:
        ans.reverse()
    
    print(*ans)

if __name__ == '__main__':
    solve()