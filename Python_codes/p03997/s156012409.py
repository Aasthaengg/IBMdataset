from sys import stdin

def I(): return int(stdin.readline().rstrip())

a,b,h = [I() for i in range(3)]

ans = int((a+b)*h/2)

print(ans)