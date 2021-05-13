import sys
row = sys.stdin.readline

def read_int(row):
    return int(row().rstrip())
  
r = read_int(row)

print(int(r **2))