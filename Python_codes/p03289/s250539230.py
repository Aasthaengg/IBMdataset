s = input()
ans = True

if s[0] != 'A':
    ans = False
    # print(f's[0]:{s[0]}')

index = -1
between_bigin_3_and_end_2 = s[2:-1]
count = between_bigin_3_and_end_2.count('C')
if count == 1:
    index = s.index('C')
    # print(index)
else:
    ans = False
    # print(f'between_bigin_3_and_end_2:{between_bigin_3_and_end_2}')
    # print(f'count:{count}')

    
for i in range(len(s)):
    if i == 0:
        continue
    if i == index:
        continue
    if not s[i].islower():
        ans = False


if ans:
    print('AC')
else:
    print('WA')