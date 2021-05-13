# https://atcoder.jp/contests/abc155/tasks/abc155_b

N = int(input())
A = list(map(int,input().split()))

def main(A):
    for a in A:
        if a%2 ==1:
            continue
        if (a%3 != 0) and (a%5 != 0):
            return "DENIED"
    return "APPROVED"

if __name__ == "__main__":
    print(main(A))