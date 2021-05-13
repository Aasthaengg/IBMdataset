from sys import stdin
s = int(stdin.readline().rstrip())
if s == 10**18:
    print(0,0,10**9,0,0,10**9)
    exit()
a = s//10**9+1
b = 10**9-s%10**9
print(0,0,10**9,1,b,a)