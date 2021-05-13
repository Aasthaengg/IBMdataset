from collections import Counter

def make_xor_sum(A):
    output = A[0]
    for i in range(1,len(A)):
        output = output ^ A[i]

    if output == 0:
        return True
    else:
        return False

def main():
    N = int(input())
    a = list(map(int,input().split()))

    if make_xor_sum(a):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
