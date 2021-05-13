A,B,C,D = map(int, input().split())
# A = int(input())
# B = int(input())
# C = int(input())
# X = input()
L = A + B
R = C + D
print("Left" if L > R else "Balanced" if L == R else "Right")