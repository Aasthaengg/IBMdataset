s = input()
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(s)) :
    if s[i] in alpha :
        alpha.remove(s[i])
if alpha :
    print(alpha[0])
else :
    print("None")
