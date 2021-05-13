a,b,c,d = map(int, input().split())
n = [0]*4
n[0] = a * c
n[1] = a * d
n[2] = b * c
n[3] = b * d

print(max(n))