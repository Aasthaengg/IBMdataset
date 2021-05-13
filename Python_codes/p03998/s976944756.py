s = [list(input()) for _ in range(3)]

n_row = 0

dic = {0:"A",1:"B",2:"C"}
s_fix = {"a":0,"b":1,"c":2}

while len(s[n_row]):    
    n_row = s_fix[s[n_row].pop(0)] 

print(dic[n_row])