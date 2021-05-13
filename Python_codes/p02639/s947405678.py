import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.readline().split())
def Li():return list(map(int,sys.stdin.readline().split()))

a = Li()
for i in range(5):
  if a[i] == 0:
    print(i+1)
    exit