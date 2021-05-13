X, Y, A, B, C = map(int, input().split(' '))

P = sorted(list(map(int, input().split(' '))), reverse=True)[:X]
Q = sorted(list(map(int, input().split(' '))), reverse=True)[:Y]
R = sorted(list(map(int, input().split(' '))), reverse=True)

apples = sorted(P + Q + R, reverse=True)[:X + Y]

print(sum(apples))
