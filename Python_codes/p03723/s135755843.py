A, B, C = map(int, input().split())
sum = 0
before = set()
while True:
    if str(A)+' '+str(B)+' '+str(C) in before:
        print(-1)
        exit()
    else:
        before.add(str(A)+' '+str(B)+' '+str(C))
    if A%2==1 or B%2==1 or C%2==1:
        print(sum)
        exit()
    temp1 = int(B/2)+int(C/2)
    temp2 = int(A/2)+int(C/2)
    temp3 = int(A/2)+int(B/2)
    A, B, C = temp1, temp2, temp3
    sum += 1