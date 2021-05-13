import sys
def slove(n, k):
    a_list = [int(i) for i in k.split()]
    num = len([i for i in a_list if i % 4 == 0])
    tmp =  [i for i in a_list if i % 4 != 0]
    num2 = len([i for i in tmp if i % 2 == 0]) // 2
    return "Yes" if (num + num2)>= n // 2 else "No"

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    k = input()
    print(slove(n, k))
