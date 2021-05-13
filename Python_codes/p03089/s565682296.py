N = int(input())
B = list(map(int, input().split()))



def solve(N,B):
    ans = []
    for _ in range(N):
        m = max(B)
        if m > len(B):
            return [-1]
        for i in range(m,0,-1):
            if B[i-1]==i:
                B.pop(i-1)
                ans.append(i)
                break
        else:
            return [-1]
    return ans
ans = solve(N,B)

print(*ans[::-1], sep='\n')