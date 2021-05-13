N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

transmitList = [A, B, C, D, E]
minTransmit = min(transmitList)

answer = 5 + N // minTransmit

if minTransmit == 1:
    answer -= 1
    
print(answer)