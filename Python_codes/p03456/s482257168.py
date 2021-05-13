import math
N = input().split()
def main():
    sum = int(N[0] + N[1])

    for i in range(1110):
        if sum == i*i:
            print("Yes")
            return
    print("No")
    return

main()
