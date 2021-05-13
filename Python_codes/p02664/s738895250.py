import sys
def Ii():return int(sys.stdin.buffer.read())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

pd = sys.stdin.readline()
print(pd.replace('?', 'D'))
