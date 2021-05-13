W = str(input()).lower() 

table = []
count = 0

while True:
    
    T = str(input())
    if T == "END_OF_TEXT":
        break
    else:
        T = T.lower().split()
    
    for j in range(len(T)):
        table.append(T[j])
    
    
for i in table:
    if i == W:
        count += 1
    
print(count)
