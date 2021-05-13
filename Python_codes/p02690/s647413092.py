X = int(input())
Ans = 0
for A in range(1,1000):
    for B in range(-A,A):
        Tar = A**5 - B**5
        if Tar == X:
            Ans = [A,B]
            break
    if Ans != 0:
        break
print(*Ans)