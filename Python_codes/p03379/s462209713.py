import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)
 
 
def main():
    N = int(input().strip())
    X_list = [int(i) for i in input().strip().split()]
    sorted_x = sorted(X_list)
 
    left = sorted_x[(N // 2)-1]
    right = sorted_x[N // 2]
    for x in X_list:
        if x <= left:
            print(right)
        else:
            print(left)
 
 
if __name__ == "__main__":
    main()