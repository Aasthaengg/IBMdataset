n = int(input())

a_list = []
person_list = []
syogen_list = []
ans = 0

for i in range(0, n):
    w = []
    v = []
    a = int(input())
    for j in range(0, a):
        x,y = map(int,input().split())
        w.append(x)
        v.append(y)
    person_list.append(w)
    syogen_list.append(v)
#print(person_list)
#print(syogen_list)

for bit in range(1 << n):
    break_flag = 0
    bit_1_cnt = 0
    for i in range(n):
        if break_flag:
            break
        if (bit >> i) & 1: #人iが正直
            for j in range(len(syogen_list[i])):
                if syogen_list[i][j] != ((bit>>(person_list[i][j]-1))&1): #矛盾　：　正直としているのに証言が食い違えばbreak
                    break_flag = 1
                    break
            bit_1_cnt += 1
        if break_flag==0 and i==n-1:
            ans = max(ans, bit_1_cnt)
print(ans)
