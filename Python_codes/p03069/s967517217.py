#laczil
def solve():
    N = int(input())
    S = input()
 
    left_black = 0
    right_white = 0
    for i in range(N):
        if S[i] == '.':
            right_white += 1
 
    ans = left_black + right_white
    for i in range(N):
        if S[i] == '#':
            left_black += 1
        else:
            right_white -= 1
        ans = min(ans, left_black + right_white)
    print(ans)
 
if __name__ == '__main__':
    solve()