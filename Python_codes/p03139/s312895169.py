N,A,B = [int(i) for i in input().split(' ')]
mx = min(A,B)
mn = max(A+B-N,0)
print(mx,mn)