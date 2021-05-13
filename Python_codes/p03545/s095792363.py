ABCD = input()
operations = []
def culc(num, ope):
    if len(ope) == 4:
        if num == 7:
            return operations.append(ope)
        else:
            return
    
    if len(ope) != 0 and ope[-1] == '+':
        num += int(ABCD[len(ope)])
    elif len(ope) != 0 and ope[-1] == '-':
        num -= int(ABCD[len(ope)])
    
    culc(num, ope+'+')
    culc(num, ope+'-')
        
culc(int(ABCD[0]), '')
ans = ''
for i in range(len(ABCD)):
    ans += ABCD[i] + operations[0][i]
print(ans[:7] + '=7')