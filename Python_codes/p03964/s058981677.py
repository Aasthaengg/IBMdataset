import math

#in1 = '5'
#in2 = ['1 2','2 1','1 1','3 1','1 1']
#n = int(in1)
n = int(input())

tall = 1
aall = 1
for idx1 in range(n):
    t, a = map(int, input().split())
    #t, a = map(int, in2[idx1].split())
    mul = max(-(-tall // t), -(-aall // a))
    tall, aall = t * mul, a * mul
    #print(tall, aall)

print(tall + aall)
