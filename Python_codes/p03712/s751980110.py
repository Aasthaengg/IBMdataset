h, w = map(int, input().split())

a = []
b = [['#' for i in range (w+2)] for j in range (h+2)] #[]で囲うことが重要


for i in range(h):
    a.append(list(input())) #splitを入れなければOK

for j in range(h):
    for k in range(w):
        b[j+1][k+1] = a[j][k]
        

for l in range(h+2):
    print("".join(b[l]))