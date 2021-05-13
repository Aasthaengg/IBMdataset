round = int(raw_input())
score = {"taro":0, "hanako":0}
counter = 0
while counter < round:
    [taro,hanako] = raw_input().split()
    if taro < hanako:
        score["hanako"] += 3
    elif taro > hanako:
        score["taro"] += 3
    else:
        score["taro"] += 1
        score["hanako"] += 1
    counter += 1

print score["taro"], score["hanako"]