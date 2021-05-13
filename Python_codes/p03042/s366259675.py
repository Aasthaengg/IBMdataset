S = input()
left = int(S[:2])
right = int(S[2:])
year_flag = [0, 0]

if left > 12 or left == 0:
    year_flag[0] += 1
if right > 12 or right == 0:
    year_flag[1] += 1

if sum(year_flag) == 2:
    print('NA')
elif sum(year_flag) == 0:
    print('AMBIGUOUS')
elif year_flag[0] == 1:
    print('YYMM')
else:
    print('MMYY')
