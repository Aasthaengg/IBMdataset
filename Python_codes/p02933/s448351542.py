import sys
def read_string(row):
    return row().rstrip()

def read_int(row):
    return int(row().rstrip())
  
row = sys.stdin.readline
a = read_int(row)
s = read_string(row)

print('red' if a < 3200 else s)