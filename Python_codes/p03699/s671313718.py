n = int(input())
ab =  [int(input()) for _ in range(n)]
abb = sorted(ab)

abc = sum(abb)

if abc %10 !=0:
    print(abc)

else:
    for i in range(n):
        if abb[i] % 10 !=0:
            print(abc-abb[i])
            exit()
    print(0)