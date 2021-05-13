N = int(input())
A = [1 if int(i)%2 else 0 for i in input().split()][::2]
print(sum(A))