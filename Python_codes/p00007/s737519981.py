from decimal import Decimal

def check(index):
    if index > len(debt_lis)-1:
        for i in range(len(debt_lis)):
            debt_lis[i] = '0'
        debt_lis.append('1')
        return
    if int(debt_lis[index]) + 1 == 10:
        return check(index+1)
    else:
        for i in range(index):
            debt_lis[i] = '0'
        num = int(debt_lis[index]) + 1
        debt_lis[index] = str(num)
        return

input_line = raw_input()
n = int(input_line)

debt = 100000
for i in range(n):
    debt = int((debt * Decimal(1.05))) 
    debt_lis = list(str(debt))
    debt_lis.reverse()
    for char_num in debt_lis[:3]:
        if not int(char_num) == 0:
            check(3)
            break
    debt_lis.reverse()
    debt = int(''.join(debt_lis))
print(debt)