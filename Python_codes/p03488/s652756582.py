S = input()
x, y = map(int, input().split())

S = S.split("T")
X_move = [len(s) for s in S[0::2]]
Y_move = [len(s) for s in S[1::2]]

x -= X_move[0]
X_move = sorted(X_move[1:])
Y_move = sorted(Y_move)

while X_move:
    mx = X_move.pop()
    if x >= 0:
        x -= mx
    else:
        x += mx

while Y_move:
    my = Y_move.pop()
    if y >= 0:
        y -= my
    else:
        y += my

if x == 0 and y == 0:
    ans = "Yes"
else:
    ans = "No"

print(ans)
