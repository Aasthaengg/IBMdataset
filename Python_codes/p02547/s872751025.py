n = int(input())
count = 0
checker = 0
while count<n:
    d1,d2 = list(map(int, input().split()))
    count += 1
    if d1==d2:
        checker += 1
        if checker ==3:
            print("Yes")
            exit()
    else:
        checker = 0
print("No")
