# [箱A, 箱B, 箱C]
list = input().split()

# 箱Aと箱B入れ替え
temp = list[0]
list[0] = list[1]
list[1] = temp

# 箱Aと箱C入れ替え
temp = list[0]
list[0] = list[2]
list[2] = temp              
              
print(' '.join(list))