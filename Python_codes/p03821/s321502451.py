N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N)]
z = 0
for a,b in AB[::-1]:
    z += -(z+a)%b
print(z)