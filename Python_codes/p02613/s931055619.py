n = int(input())
c0 = 0
c1 = 0
c2 = 0
c3 = 0

#縦に文字列を複数入力　＆　操作
for i in range(n):
    s = input()
    if s == "AC":
        c0 += 1
    if s == "WA":
        c1 += 1
    if s == "TLE":
        c2 += 1
    if s == "RE":
        c3 += 1    
        
print('AC x ',end='')
print(c0)
print('WA x ',end='')
print(c1)
print('TLE x ',end='')
print(c2)
print('RE x ',end='')
print(c3)