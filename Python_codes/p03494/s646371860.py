a = int(input())
b = [int(i) for i in input().split(" ")]
count = 0
iti = 1
while iti == 1:
    for i in range(a):
        if b[i]%2 == 0:
            b[i]=b[i]//2
            iti = 1
        else :
            print(count)
            iti = 0
            break
    count = count+1