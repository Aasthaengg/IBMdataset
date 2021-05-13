import sys
input = sys.stdin.readline

def main():
    H, W, A, B = [int(x) for x in input().split()]

    ans = [[0] * W for j in range(H)]


    for j in range(H):
        if B > 0:
            for i in range(A):
                ans[j][i] = 1
            B -= 1
        else:
            for i in range(A, W):
                ans[j][i] = 1



    for j in range(H):
        print("".join(map(str, ans[j])))




    

if __name__ == '__main__':
    main()

