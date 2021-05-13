import sys;input = lambda : sys.stdin.readline()
n = int(input())
div,mod=divmod(n,11)
print(div*2 if mod==0 else (div*2+1 if mod<=6 else div*2+2))