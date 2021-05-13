n = input()
n = n.replace('9', 'x').replace('1', '9').replace('x', '1')
print(n)

'''
n = list(input())
for i in range(3):
    if n[i] == '1':
        n[i] = '9'
    elif n[i] == '9':
        n[i] = '1'
print("".join(n))
'''
