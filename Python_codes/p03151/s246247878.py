def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans = 0

    remain = []
    lack = 0
    for i in range(N):
        diff = A[i] - B[i]
        if diff > 0:
            remain.append(diff)
        if diff < 0:
            lack += abs(diff)
            ans += 1

    if lack == 0:
        print("0")
        return
    
    remain.sort(reverse=True)
    sm = 0
    for r in remain:
        sm += r
        ans += 1
        if sm >= lack:
            print(ans)
            break
    else:
        print("-1")
    
if __name__ == '__main__':
    solve()