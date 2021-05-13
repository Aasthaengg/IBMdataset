P, Q, R = map(int, input().split())

PQ = P+Q
PR = P+R
QR = Q+R

print(min([PQ,PR,QR]))