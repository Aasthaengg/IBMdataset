S=input()
w=int(input())

Q=''
import math
for i in range(math.ceil(len(S)/w)):
    Q+=S[i*w]
print(Q)