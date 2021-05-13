X, K, D = map(int, input().split())

X = abs(X)

candidate1 = abs(X - K*D)
candidate2 = abs(X % D)
candidate3 = candidate2 - D

count2 = (X - candidate2)//D
if (K - count2) % 2==0:
    count2ok = True
else:
    count2ok = False


count3 = (X - candidate3)//D
if (K - count3) % 2==0:
    count3ok = True
else:
    count3ok = False

candidate3 = abs(candidate3)

if abs(X) - K*D > 0:
    print(candidate1)
elif count2ok == True and count3ok == True:
    print(min([candidate1, candidate2, candidate3]))
elif count2ok == True:
    print(min([candidate1, candidate2]))
elif count3ok == True:
    print(min([candidate1, candidate3]))
else:
    print(candidate1)