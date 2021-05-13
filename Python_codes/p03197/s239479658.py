def solve():
    N = int(input())
    for _ in range(N):
        if int(input()) % 2 != 0:
            print("first")
            return
    else:
        print("second")
    
if __name__ == '__main__':
    solve()