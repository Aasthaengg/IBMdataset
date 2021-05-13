N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

def main():
    cur = 0
    ans = 0

    if A[0] != 0:
        print(-1)
        return

    for a in A:
        if a <= cur:
            ans += a
        elif a == cur+1:
            ans += 1
        else:
            print(-1)
            return
        cur = a

    print(ans)

    
main()