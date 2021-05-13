s = input()
num = len(s)

kb = []

for i in range(num):
    kb.append(s[i])

mae = 0
usi = num-1
ans = 0

while mae < usi:
    #print(i)
    if s[mae] != s[usi]:
        if s[mae] == 'x':
            #kb.append('x')
            ans += 1
            mae += 1
        elif s[usi] == 'x':
            #kb.insert(mae,'x')
            ans += 1
            usi -= 1
        else:
            print(-1)
            exit()
    else:
        mae += 1
        usi -= 1

print(ans)