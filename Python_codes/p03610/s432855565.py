def actual(s):
    answer = ''

    for idx, c in enumerate(s):
        if idx % 2 == 0:
            answer += c

    return answer

s = input()

print(actual(s))