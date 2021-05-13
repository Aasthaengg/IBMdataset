Answer = input()
input_retu = input()
count = 0
for i in range(len(Answer)):
    if Answer[i] == input_retu[i]:
        continue
    else:
        count += 1
print(count)