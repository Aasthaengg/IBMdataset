S = input()
q = int(input())

ans = S
for _ in range(q):
    A = input().split()
    if A[0]=='print':
        a,b = map(int, A[1:])
        print(ans[a:b+1])
    elif A[0]=='reverse':
        a,b = map(int, A[1:])
        ans = ans[:a] + ans[a:b+1][::-1] + ans[b+1:]
    elif A[0]=='replace':
        a,b = map(int, A[1:3])
        p = A[3]
        ans = ans[:a] + p + ans[b+1:]
