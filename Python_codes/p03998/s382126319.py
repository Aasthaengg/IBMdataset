s = [list(input()) for _ in range(3)]

n_row = 0

dic = {0:"A",1:"B",2:"C"}

while len(s[n_row]):
    s_num = s[n_row].pop(0)
    
    if s_num == "a":
        n_row = 0
    elif s_num == "b":
        n_row = 1
    elif s_num =="c":
        n_row = 2

print(dic[n_row])