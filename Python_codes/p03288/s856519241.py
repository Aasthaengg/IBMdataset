import sys
input = sys.stdin.readline
R = int(input())
if R < 1200 :
    print("ABC")
elif R >= 1200 and R < 2800 :
    print("ARC")
else :
    print("AGC")