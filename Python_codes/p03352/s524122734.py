X = int(input())
if X==1:
    MAX = 1
else:
    MAX = 0
    for B in range(2,35):
        for P in range(2,15):
            if B**P>X:
                break
            else:
                if MAX<B**P:
                    MAX = B**P
print(MAX)