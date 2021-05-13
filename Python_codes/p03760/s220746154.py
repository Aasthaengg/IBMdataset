o = list(input())
e = list(input())

passw = [""]
for i in range(len(e)):
    passw.append(o[i])
    passw.append(e[i])
    
if len(o)>len(e):
    passw.append(o[-1])
    
print(''.join(passw))