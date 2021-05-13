i=1
import copy
X=int(input())
s=0
while True:
    s+=copy.copy(i)
    if s>=X:
        print(i)
        exit()
    i+=1
