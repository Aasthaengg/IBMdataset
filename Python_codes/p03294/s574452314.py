N = int(input())
A = list(map(int, input().split()))
 
ans = [a - 1 for a in A]
print(sum(ans))