l = list(map(int, input().split()))
s = ''
s += 'U'*(l[3]-l[1])
s += 'R'*(l[2]-l[0])
s += 'D'*(l[3]-l[1])
s += 'L'*(l[2]-l[0])
s += 'L'
s += 'U'*(l[3]-l[1]+1)
s += 'R'*(l[2]-l[0]+1)
s += 'D'
s += 'R'
s += 'D'*(l[3]-l[1]+1)
s += 'L'*(l[2]-l[0]+1)
s += 'U'
print(s)
