# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
a,b,c,d = map(int,input().split())

print("Yes" if abs(a-c)<=d or (abs(a-b)<=d and abs(b-c)<=d) else "No")