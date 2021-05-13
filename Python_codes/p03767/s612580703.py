n = int(input())
A = sorted(map(int, input().split()), reverse=True)
print(sum(A[1::2][:n]))
