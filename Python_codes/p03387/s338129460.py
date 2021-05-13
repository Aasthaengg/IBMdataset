#C - Same Integers
ABC = list(map(int,input().split()))
ABC = sorted(ABC,reverse = True)
A = ABC[0]#max
B = ABC[1]
C = ABC[2]#min
count = 0
while A != B:
    C += 1
    B += 1
    count += 1
while (B - C)%2 == 1:
    A += 1
    B += 1
    count += 1
while A!=C:
    C += 2
    count += 1
print(count)