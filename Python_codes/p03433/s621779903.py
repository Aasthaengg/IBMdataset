N = int(input())
A = int(input())#1 yen
print('Yes' if N % 500 == 0 or (N % 500) <= A else 'No')