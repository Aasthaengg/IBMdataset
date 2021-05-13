n = int(input())

for i in range(n,1000):
    one = i % 10
    ten = i //10 % 10
    hund = i // 100
    if one == ten and ten == hund:
        print(hund*100+ten*10+one)
        break
