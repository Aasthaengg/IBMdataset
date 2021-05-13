N, A, B = map(int, input().split())
mini = max(0,A+B-N)
maxi = min(A,B)
print(*[maxi,mini])