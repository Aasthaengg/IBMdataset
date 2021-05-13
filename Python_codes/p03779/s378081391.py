X = int(input())
ans = (-1 + (1+8*X)**(1/2)) / 2
if ans % 1 <= 10**(-7):
    print(int(ans))
else:
    print(int(1 + ans//1))