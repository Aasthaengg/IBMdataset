string=[]
W = input()#単語入力
while True:
    T = input()#入力
    if T == 'END_OF_TEXT':#EOT入力のときループぬける
        break
    string.append(T)#list追加
count=0
for i in range(len(string)):
    string[i]=string[i].lower()
    string[i] = string[i].split(" ")
    for j in range(len(string[i])):
        if W == string[i][j]:
            count+=1
print(count)
