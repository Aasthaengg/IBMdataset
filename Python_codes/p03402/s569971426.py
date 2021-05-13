A,B=map(int,input().split())

g=[["#"]*100 for _ in range(50)] +[['.']*100 for _ in range(50)]


for i in range(A-1):
    x=(i%50)*2
    y=(i//50)*2
    g[y][x]="."

for i in range(B-1):
    x=(i%50)*2
    y=51+(i//50)*2
    g[y][x]="#"

print(100,100)
for n in g:
    print("".join(n))