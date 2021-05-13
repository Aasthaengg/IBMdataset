#153_D
h = int(input())

count = 0
monster = 1
while h > 0:
    h = h // 2
    count += monster
    monster *= 2

print(count)