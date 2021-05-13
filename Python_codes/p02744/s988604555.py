N = int(input())
answers = []

def cal(already_used, answer):
    if len(answer) == N:
        answers.append(answer)
        return

    if len(already_used) == 0:
        plus_1 = 0
    else:
        plus_1 = max(already_used) + 1

    cur_target = already_used + [plus_1]
    for c in cur_target:
        _answer = answer + str(c)
        if c != plus_1:
            _answer = cal(already_used, _answer)
        else:
            _answer = cal(cur_target, _answer)


cal([], "")
for answer in answers:
    for (num, alp) in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]):
        answer = answer.replace(str(num), alp)
    print(answer)