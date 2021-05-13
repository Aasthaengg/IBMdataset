N = int(input())
A = list(map(int, input().split()))

ans = len(set(A))-(len(A)-len(set(A)))%2

print(ans)