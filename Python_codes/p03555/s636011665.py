first = input()
second = input()

row_1 = [w for w in first]
row_2 = [w for w in second]

if row_1[0] == row_2[2] and row_1[1] == row_2[1] and row_1[2] == row_2[0]:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)