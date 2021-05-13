s = input()
k = int(input())
count = 0
for i in range(len(s)) :
    if s[i] == "1" :
        count += 1
    else :
        break
if k > count :
    print(s[count])
else :
    print("1")