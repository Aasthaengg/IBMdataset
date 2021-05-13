def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    aj = A.pop()
    A.sort(key=lambda x: abs(aj / 2 - x))
    print(aj, A[0]) 
main()
