P,Q,R = map(int,input().split())

PR = P + R
QR = Q + R
QP = Q + P

ans = min(PR,min(QR,QP))

print(ans)