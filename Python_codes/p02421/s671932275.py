score = {"taro":0, "hanako":0}
n = int(input())

for i in range(n):
    words = input().split()

    if words[0] > words[1]:
        score["taro"] += 3
    elif words[0] < words[1]:
        score["hanako"] += 3
    else:
        score["taro"] += 1
        score["hanako"] += 1

print(score["taro"], score["hanako"])