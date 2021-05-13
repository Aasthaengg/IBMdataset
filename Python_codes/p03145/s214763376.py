A,B,C = map(int,input().split())

maxL = max(A,B,C)
minL = min(A,B,C)
midium = A+B+C - maxL - minL

print(int(minL*midium/2))