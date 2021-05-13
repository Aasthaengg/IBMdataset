from math import ceil
def solve():
    N,D,A = map(int,input().split())
    monster = []
    for i in range(N):
        x,h = map(int,input().split())
        monster.append([x,h])
    
    monster.sort(key=lambda x:x[0])

    S = [0] * (N+1)
    ans = 0
    for i in range(N):
        if S[i] < monster[i][1]:
            left = i-1
            right = N
            while right - left > 1:
                mid = (left + right) // 2
                if monster[mid][0] > monster[i][0] + 2 * D:
                    right = mid
                else:
                    left = mid
            include_end = left
            need = ceil((monster[i][1] - S[i]) / A)
            S[i] += need * A
            S[include_end+1] -= need * A
            ans += need
        S[i+1] += S[i]
    
    print(ans)

if __name__ == '__main__':
    solve()