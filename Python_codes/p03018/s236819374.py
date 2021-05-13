s=input()
s=s.replace('BC','.')
s=s.replace('B','/')
s=s.replace('C','/')
sl = s.split('/')
cnt =0
for si in sl:
    incre = 0
    for ci in si:
        if ci == 'A':
            incre +=1
        if ci == '.':
            cnt += incre
print(cnt)
