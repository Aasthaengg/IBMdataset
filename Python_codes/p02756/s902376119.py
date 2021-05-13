import sys
input = sys.stdin.readline

c = input()
c = c[:len(c)-1]
q = int(input())

num = len(c)
c_mae = ''
c_ato = ''

hantei = 1

for i in range(q):
    q_i= list(input())
    #print(q_i)
    if q_i[0] == '1':
        hantei *= -1
    elif (q_i[2] =='1' and hantei == 1) or (q_i[2] == '2' and hantei == -1):
        c_mae = q_i[4] + c_mae
    else:
        c_ato += q_i[4]

print(c_mae+c+c_ato if hantei == 1 else (c_mae+c+c_ato)[::-1])
