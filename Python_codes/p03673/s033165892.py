N = int(input())
A = input().split()
print(*(A[::-2]+A[N%2::2]))