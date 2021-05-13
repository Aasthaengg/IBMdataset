N = int(input())
s12 = [list(input()), list(input())]
index = 0
left_block = None
point_dict = {"X": {"X": 2, "Y": 1}, "Y": {"X": 2, "Y": 3}}
point = 1
n3 = 0
n2 = 0
n1 = 0
while True:
    if index >= N:
        break
    if left_block:
        if s12[0][index] == s12[1][index]:
            now_block = "X"
            index += 1
        else:
            now_block = "Y"
            index += 2
        point *= point_dict[now_block][left_block]
        left_block = now_block
    else:
        if s12[0][0] == s12[1][0]:
            left_block = "X"
            index += 1
            point *= 3
        else:
            left_block = "Y"
            index += 2
            point *= 6

print(point % (10**9 + 7))
