inversion = 1 #1 は反転していない、 -1 は反転している。
s = input()
s1 = ""
s2 = ""
n_query = int(input())
for i in range(n_query):
    q = input().split()
    
    if q[0] == '1':
        inversion *= -1
    elif q[0] == '2':
        if inversion == 1:
            if q[1] == '1':
                s1 = s1 + q[2]
            elif q[1] == '2':
                s2 = s2 + q[2]
        elif inversion == -1:
            if q[1] == '1':
                s2 = s2 + q[2]
            elif q[1] == '2':
                s1 = s1 + q[2]

if inversion == 1:
    s = s1[::-1] + s + s2
elif inversion == -1:
    s = s2[::-1] + s[::-1] + s1

print(s)