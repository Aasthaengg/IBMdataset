N,A,B = list(map(int,input().split()))
MIN = A*(N-1)+B
MAX = A+B*(N-1)
print(max(MAX-MIN+1,0))
