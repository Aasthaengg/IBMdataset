import math
def main():
    N, K = map(int, input().split())
    count = 0
    flag = True
    while flag:
        if N - K < 0:
            flag = False
        else:
            N -= 1
            count += 1
    print(count)
main()
