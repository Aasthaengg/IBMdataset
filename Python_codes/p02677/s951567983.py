import math
A,B,H,M = map(int, input().split())
H = 60*H + M
pi = (math.pi/180)
HP = [A*math.cos(0.5*H*pi), A*math.sin(0.5*H*pi)]
MP = [B*math.cos(6*M*pi), B*math.sin(6*M*pi)]

print(math.sqrt((HP[0]-MP[0])**2 + (HP[1]-MP[1])**2))


