import sys
N = int(input())
if N < 10 or N > 99:
    sys.exit()

if int(str(N)[0:1]) == 9 or int(str(N)[-1]) == 9:
    print("Yes")
else:
    print("No")