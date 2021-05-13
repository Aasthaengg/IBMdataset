a,b=map(int,input().split())
s=[["#" for i in range(100)] for j in range(50)]
t=[["." for i in range(100)] for j in range(50)]

a2,a3=(a-1)//50,(a-1)%50
for i in range(0,2*a2,2):
    for j in range(0,100,2):
        s[i][j]="."
for i in range(0,2*a3,2):
    s[2*a2][i]="."

b2,b3=(b-1)//50,(b-1)%50
for i in range(2,2*b2+2,2):
    for j in range(0,100,2):
        t[i][j]="#"
for i in range(0,2*b3,2):
        t[2*b2+2][i]="#"
print(100,100)
for i in range(50):
    print("".join(s[i]))
for i in range(50):
    print("".join(t[i]))