X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)

temp = P[:X] + Q[:Y] + R

temp.sort(reverse=True)
ans = sum(temp[:X+Y])

print(ans)