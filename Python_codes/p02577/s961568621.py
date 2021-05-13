N = str(input())
s = 0
if len(N) == 1:
    n = int(N)
    if n % 9 ==0:
        print("Yes")
    else:
        print("No")
else:
    for i in range(len(N)):
        s += int(N[-i+1])
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")