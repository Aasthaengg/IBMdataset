T,A,S = map(int, input().split(' '))

persons = [T, A, S]

def check_even(persons):
    for person in persons:
        if person % 2 != 0:
            return False
    return True

# 1 1 1 の判定を先にするため

# 0回目
if not check_even(persons):
    print(0)
    exit()

# 全数同値 -> 無限
if T == A and A == S:
    print(-1)
    exit()

count = 1

while True:
    for person in persons:
        tmp_0 = persons[0]
        tmp_1 = persons[1]
        tmp_2 = persons[2]

        persons[0] = 0 + tmp_1 / 2 + tmp_2 / 2
        persons[1] = tmp_0 / 2 + 0 + tmp_2 / 2
        persons[2] = tmp_0 / 2 + tmp_1 / 2 + 0

        if check_even(persons):
            count += 1
        else:
            print(count)
            exit()
