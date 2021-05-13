N,A,B = map(int,input().split())

left = A*(N-1)+B
right = A + (N-1)*B
print(max(0,right-left+1))