A, B, C, D = map(int, input().split())

while True:
    if C - B >0:
        C -= B
    else:
        print("Yes")
        exit()
    if A - D >0:
        A -= D
    else:
        print("No")
        exit()