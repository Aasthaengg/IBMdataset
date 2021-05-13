while True:
    number = input()
    if number == "0":
        break
    else:
        number2 = []
        for i in range(len(number)):
            number2.append(number[i])

        number2 = map(int, number2)
        answer = sum(number2)

        print(answer)