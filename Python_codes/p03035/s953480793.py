age, fee = map(int, input().split())

if 13 <= age:
    print(fee)
elif 6 <= age  and age <= 12:
    print(fee // 2)
elif age < 6:
    print(0)